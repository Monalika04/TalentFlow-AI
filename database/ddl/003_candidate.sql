CREATE TABLE core.candidate (

    candidate_id BIGSERIAL,

    first_name VARCHAR(100) NOT NULL,

    last_name VARCHAR(100) NOT NULL,

    email VARCHAR(255) NOT NULL,

    phone VARCHAR(20) NOT NULL,

    city VARCHAR(100) NOT NULL,

    state VARCHAR(100) NOT NULL,

    country VARCHAR(100) NOT NULL,

    total_experience NUMERIC(4,1) NOT NULL DEFAULT 0,

    current_ctc NUMERIC(10,2) NOT NULL DEFAULT 0,

    expected_ctc NUMERIC(10,2) NOT NULL DEFAULT 0,

    notice_period_days INTEGER NOT NULL DEFAULT 0,

    highest_education VARCHAR(100) NOT NULL,

    linkedin_url TEXT,

    github_url TEXT,

    portfolio_url TEXT,

    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_candidate
        PRIMARY KEY (candidate_id),

    CONSTRAINT uq_candidate_email
        UNIQUE (email),

    CONSTRAINT uq_candidate_phone
        UNIQUE (phone),

    CONSTRAINT chk_candidate_status
        CHECK (status IN ('ACTIVE', 'HIRED', 'REJECTED', 'ON_HOLD')),

    CONSTRAINT chk_candidate_experience
        CHECK (total_experience >= 0),

    CONSTRAINT chk_candidate_current_ctc
        CHECK (current_ctc >= 0),

    CONSTRAINT chk_candidate_expected_ctc
        CHECK (expected_ctc >= current_ctc),

    CONSTRAINT chk_candidate_notice
        CHECK (notice_period_days >= 0)

);