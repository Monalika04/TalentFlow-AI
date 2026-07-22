CREATE TABLE core.skill (

    skill_id BIGSERIAL,

    skill_name VARCHAR(100) NOT NULL,

    category VARCHAR(50) NOT NULL,

    description TEXT,

    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_skill
        PRIMARY KEY (skill_id),

    CONSTRAINT uq_skill_name
        UNIQUE (skill_name),

    CONSTRAINT chk_skill_status
        CHECK (status IN ('ACTIVE', 'INACTIVE'))

);