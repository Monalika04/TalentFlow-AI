CREATE TABLE core.job_skill (

    job_skill_id BIGSERIAL,

    job_id BIGINT NOT NULL,

    skill_id BIGINT NOT NULL,

    importance_weight INTEGER NOT NULL DEFAULT 3,

    is_mandatory BOOLEAN NOT NULL DEFAULT FALSE,

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_job_skill
        PRIMARY KEY (job_skill_id),

    CONSTRAINT fk_job_skill_job
        FOREIGN KEY (job_id)
        REFERENCES core.job(job_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_job_skill_skill
        FOREIGN KEY (skill_id)
        REFERENCES core.skill(skill_id)
        ON DELETE RESTRICT,

    CONSTRAINT uq_job_skill
        UNIQUE(job_id, skill_id),

    CONSTRAINT chk_importance_weight
        CHECK (importance_weight BETWEEN 1 AND 5)

);