CREATE TABLE core.recruiter (

    recruiter_id BIGSERIAL PRIMARY KEY,

    company_id BIGINT NOT NULL,

    first_name VARCHAR(100) NOT NULL,

    last_name VARCHAR(100) NOT NULL,

    email VARCHAR(255) NOT NULL UNIQUE,

    password_hash TEXT NOT NULL,

    role VARCHAR(20) NOT NULL,

    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',

    last_login TIMESTAMPTZ,

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_recruiter_company
        FOREIGN KEY (company_id)
        REFERENCES core.company(company_id),

    CONSTRAINT chk_recruiter_role
        CHECK (
            role IN (
                'ADMIN',
                'RECRUITER'
            )
        ),

    CONSTRAINT chk_recruiter_status
        CHECK (
            status IN (
                'ACTIVE',
                'INACTIVE'
            )
        )
);