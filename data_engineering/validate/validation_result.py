from dataclasses import dataclass


@dataclass
class ValidationResult:

    validation_name: str

    passed: bool

    total_rows: int

    failed_rows: int

    message: str