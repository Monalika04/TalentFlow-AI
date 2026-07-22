CREATE TABLE core.candidate_skill (

    candidate_skill_id BIGSERIAL,

    candidate_id BIGINT NOT NULL,

    skill_id BIGINT NOT NULL,

    proficiency_level VARCHAR(20) NOT NULL,

    years_experience NUMERIC(4,1) NOT NULL DEFAULT 0,

    last_used DATE,

    is_primary BOOLEAN NOT NULL DEFAULT FALSE,

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_candidate_skill
        PRIMARY KEY (candidate_skill_id),

    CONSTRAINT fk_candidate_skill_candidate
        FOREIGN KEY (candidate_id)
        REFERENCES core.candidate(candidate_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_candidate_skill_skill
        FOREIGN KEY (skill_id)
        REFERENCES core.skill(skill_id)
        ON DELETE RESTRICT,

    CONSTRAINT uq_candidate_skill
        UNIQUE(candidate_id, skill_id),

    CONSTRAINT chk_candidate_skill_proficiency
        CHECK (
            proficiency_level IN (
                'BEGINNER',
                'INTERMEDIATE',
                'ADVANCED',
                'EXPERT'
            )
        ),

    CONSTRAINT chk_candidate_skill_experience
        CHECK (years_experience >= 0)

);