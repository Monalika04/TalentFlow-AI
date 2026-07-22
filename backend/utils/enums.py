from enum import Enum


class Status(str, Enum):

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"


class JobStatus(str, Enum):

    OPEN = "OPEN"

    CLOSED = "CLOSED"


class ApplicationStatus(str, Enum):

    APPLIED = "APPLIED"

    SCREENING = "SCREENING"

    INTERVIEW = "INTERVIEW"

    OFFERED = "OFFERED"

    HIRED = "HIRED"

    REJECTED = "REJECTED"

    WITHDRAWN = "WITHDRAWN"


class RecommendationType(str, Enum):

    STRONG_MATCH = "STRONG_MATCH"

    GOOD_MATCH = "GOOD_MATCH"

    PARTIAL_MATCH = "PARTIAL_MATCH"

    NOT_RECOMMENDED = "NOT_RECOMMENDED"