from backend.ai.parser_schema import ResumeAIResponse


class PromptBuilder:
    """
    Builds the prompt sent to Gemini for resume analysis.
    """

    def build_prompt(self, resume_text: str) -> str:
        sections = [
            self._system_role(),
            self._task(),
            self._rules(),
            self._schema(),
            self._resume(resume_text),
        ]

        return "\n\n".join(sections)

    def _system_role(self) -> str:
        return """
You are TalentFlow AI, an expert Recruitment Intelligence Assistant.

Your job is to analyze professional resumes with high accuracy.

Separate factual information from AI-generated intelligence.

Never fabricate information.
"""

    def _task(self) -> str:
        return """
TASK

Analyze the provided resume and return exactly two sections:

1. facts
2. intelligence
"""

    def _rules(self) -> str:
        return """
RULES

- Return ONLY valid JSON.
- Do not return Markdown.
- Do not wrap JSON inside code blocks.
- Do not include explanations.
- Never invent information.
- If information is unavailable, return null or an empty list.
- Keep factual extraction and AI reasoning separate.
- Follow the provided schema exactly.
"""

    def _schema(self) -> str:
        return f"""
EXPECTED JSON SCHEMA

{ResumeAIResponse.model_json_schema()}
"""

    def _resume(self, resume_text: str) -> str:
        return f"""
RESUME

{resume_text}
"""