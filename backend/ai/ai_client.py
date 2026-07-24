import json
import logging
import time

from google import genai
from google.genai import types

from backend.ai.parser_schema import ResumeAIResponse

logger = logging.getLogger(__name__)


class AIResponseError(Exception):
    """Raised when Gemini returns an invalid response."""
    pass


class GeminiClient:

    MAX_RETRIES = 3
    TIMEOUT = 60

    def __init__(self, api_key: str):

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-3.6-flash"

    def generate(self, prompt: str) -> ResumeAIResponse:

        last_exception = None

        for attempt in range(1, self.MAX_RETRIES + 1):

            try:

                start_time = time.time()

                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.1,
                        response_mime_type="application/json",
                    ),
                )

                execution_time = time.time() - start_time

                logger.info(
                    "Gemini response received in %.2f seconds",
                    execution_time,
                )

                cleaned = self._clean_response(response.text)

                parsed = self._parse_json(cleaned)

                return ResumeAIResponse.model_validate(parsed)

            except Exception as exc:

                last_exception = exc

                logger.warning(
                    "Gemini attempt %s failed: %s",
                    attempt,
                    str(exc),
                )

                if attempt < self.MAX_RETRIES:
                    time.sleep(2 ** (attempt - 1))

        raise AIResponseError(str(last_exception))

    def _clean_response(self, text: str) -> str:

        text = text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")

        if text.endswith("```"):
            text = text[:-3]

        return text.strip()

    def _parse_json(self, text: str) -> dict:

        try:
            return json.loads(text)

        except json.JSONDecodeError as exc:
            raise AIResponseError(
                "Gemini returned invalid JSON."
            ) from exc