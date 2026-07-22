INSERT INTO core.candidate_skill
(
    candidate_id,
    skill_id,
    proficiency_level,
    years_experience,
    last_used,
    is_primary
)
VALUES
(1, 1, 'ADVANCED', 2.0, '2026-07-20', TRUE),       -- Python
(1, 2, 'ADVANCED', 2.0, '2026-07-20', TRUE),       -- SQL
(1, 4, 'INTERMEDIATE', 1.5, '2026-07-15', FALSE),  -- Power BI
(1, 3, 'INTERMEDIATE', 1.5, '2026-07-18', FALSE),  -- PostgreSQL
(1, 5, 'ADVANCED', 4.0, '2026-07-20', FALSE);      -- Excel