import re
from pathlib import Path

import pdfplumber
from docx import Document


class ResumeParsingError(Exception):
    """
    Raised when resume parsing fails.
    """
    pass


class ResumeParser:
    """
    Responsible for extracting clean text from resume files.

    Supported formats:
    - PDF
    - DOCX
    """

    SUPPORTED_EXTENSIONS = {".pdf", ".docx"}

    def extract_text(self, file_path: str) -> str:
        """
        Extract text from a supported resume file.
        """

        path = Path(file_path)

        if not path.exists():
            raise ResumeParsingError(
                f"Resume file not found: {file_path}"
            )

        extension = path.suffix.lower()

        if extension not in self.SUPPORTED_EXTENSIONS:
            raise ResumeParsingError(
                f"Unsupported file type: {extension}"
            )

        try:

            if extension == ".pdf":
                text = self._extract_pdf_text(path)

            else:
                text = self._extract_docx_text(path)

            cleaned_text = self._clean_text(text)

            if not cleaned_text:
                raise ResumeParsingError(
                    "No text could be extracted from the resume."
                )

            return cleaned_text

        except Exception as e:
            raise ResumeParsingError(str(e)) from e

    def _extract_pdf_text(self, path: Path) -> str:
        """
        Extract text from PDF using pdfplumber.
        """

        pages = []

        with pdfplumber.open(path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    pages.append(page_text)

        return "\n".join(pages)

    def _extract_docx_text(self, path: Path) -> str:
        """
        Extract text from DOCX.
        """

        document = Document(path)

        paragraphs = []

        for paragraph in document.paragraphs:

            text = paragraph.text.strip()

            if text:
                paragraphs.append(text)

        return "\n".join(paragraphs)

    def _clean_text(self, text: str) -> str:
        """
        Normalize extracted resume text.
        """

        text = text.replace("\xa0", " ")

        text = re.sub(r"[ \t]+", " ", text)

        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()