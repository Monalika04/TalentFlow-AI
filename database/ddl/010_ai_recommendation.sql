CREATE TABLE ai.ai_recommendation (

    recommendation_id BIGSERIAL,

    application_id BIGINT NOT NULL,

    overall_score NUMERIC(5,2) NOT NULL,

    skill_score NUMERIC(5,2) NOT NULL,

    experience_score NUMERIC(5,2) NOT NULL,

    education_score NUMERIC(5,2) NOT NULL,

    confidence_score NUMERIC(5,2) NOT NULL,

    missing_skills TEXT,

    strengths TEXT,

    recommendation VARCHAR(20) NOT NULL,

    reasoning TEXT,

    model_version VARCHAR(20) NOT NULL,

    generated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_ai_recommendation
        PRIMARY KEY (recommendation_id),

    CONSTRAINT fk_ai_application
        FOREIGN KEY (application_id)
        REFERENCES core.application(application_id)
        ON DELETE CASCADE,

    CONSTRAINT uq_ai_application
        UNIQUE(application_id),

    CONSTRAINT chk_overall_score
        CHECK (overall_score BETWEEN 0 AND 100),

    CONSTRAINT chk_skill_score
        CHECK (skill_score BETWEEN 0 AND 100),

    CONSTRAINT chk_experience_score
        CHECK (experience_score BETWEEN 0 AND 100),

    CONSTRAINT chk_education_score
        CHECK (education_score BETWEEN 0 AND 100),

    CONSTRAINT chk_confidence_score
        CHECK (confidence_score BETWEEN 0 AND 100),

    CONSTRAINT chk_recommendation
        CHECK (
            recommendation IN
            (
                'STRONG_MATCH',
                'GOOD_MATCH',
                'PARTIAL_MATCH',
                'NOT_RECOMMENDED'
            )
        )

);