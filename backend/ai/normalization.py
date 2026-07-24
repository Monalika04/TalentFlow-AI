from typing import Dict


SKILL_ALIASES: Dict[str, str] = {
    "python": "Python",
    "py": "Python",

    "sql": "SQL",

    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",

    "mysql": "MySQL",

    "power bi": "Power BI",
    "powerbi": "Power BI",

    "excel": "Microsoft Excel",

    "javascript": "JavaScript",
    "js": "JavaScript",

    "nodejs": "Node.js",
    "node.js": "Node.js",

    "fastapi": "FastAPI",

    "pandas": "Pandas",

    "numpy": "NumPy",

    "scikit learn": "Scikit-learn",
    "sklearn": "Scikit-learn",
}


def normalize_skill(skill: str) -> str:
    """
    Normalize technical skill names.
    """

    normalized = skill.strip().lower()

    return SKILL_ALIASES.get(normalized, skill.strip())


def normalize_skill_list(skills: list[str]) -> list[str]:
    """
    Normalize an entire skill list and remove duplicates.
    """

    normalized = [
        normalize_skill(skill)
        for skill in skills
    ]

    unique = sorted(set(normalized))

    return unique