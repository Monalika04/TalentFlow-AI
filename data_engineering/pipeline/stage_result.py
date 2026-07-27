from dataclasses import dataclass


@dataclass
class StageResult:

    name: str

    status: str

    rows: int

    execution_time: float

    data: dict