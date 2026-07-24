import os
import uuid
from decimal import Decimal
from pathlib import Path

from fastapi import HTTPException, UploadFile


class FileService:

    ALLOWED_EXTENSIONS = {"pdf", "docx"}

    UPLOAD_DIRECTORY = Path("backend/uploads/resumes")

    @classmethod
    def initialize(cls):
        cls.UPLOAD_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True,
        )

    @classmethod
    async def save_resume(
        cls,
        file: UploadFile,
    ):

        cls.initialize()

        extension = file.filename.split(".")[-1].lower()

        if extension not in cls.ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail="Only PDF and DOCX files are allowed.",
            )

        unique_filename = (
            f"{uuid.uuid4()}.{extension}"
        )

        file_path = (
            cls.UPLOAD_DIRECTORY / unique_filename
        )

        contents = await file.read()

        with open(file_path, "wb") as f:
            f.write(contents)

        file_size_kb = Decimal(
            round(len(contents) / 1024, 2)
        )

        return {
            "file_name": unique_filename,
            "original_name": file.filename,
            "file_path": str(file_path),
            "file_type": extension.upper(),
            "file_size_kb": file_size_kb,
        }

    @classmethod
    def delete_resume(
        cls,
        file_path: str,
    ):

        if os.path.exists(file_path):
            os.remove(file_path)