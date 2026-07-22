CREATE TABLE core.application (

    application_id BIGSERIAL,

    candidate_id BIGINT NOT NULL,

    job_id BIGINT NOT NULL,

    application_date TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    application_status VARCHAR(20) NOT NULL DEFAULT 'APPLIED',

    ai_match_score NUMERIC(5,2),

    recruiter_notes TEXT,

    source VARCHAR(50),

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_application
        PRIMARY KEY (application_id),

    CONSTRAINT fk_application_candidate
        FOREIGN KEY (candidate_id)
        REFERENCES core.candidate(candidate_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_application_job
        FOREIGN KEY (job_id)
        REFERENCES core.job(job_id)
        ON DELETE CASCADE,

    CONSTRAINT uq_candidate_job
        UNIQUE(candidate_id, job_id),

    CONSTRAINT chk_application_status
        CHECK (
            application_status IN (
                'APPLIED',
                'SCREENING',
                'INTERVIEW',
                'OFFERED',
                'HIRED',
                'REJECTED',
                'WITHDRAWN'
            )
        ),

    CONSTRAINT chk_ai_match_score
        CHECK (
            ai_match_score IS NULL
            OR (ai_match_score BETWEEN 0 AND 100)
        )

);