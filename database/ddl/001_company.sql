CREATE TABLE core.company (

    company_id BIGSERIAL,

    company_name VARCHAR(150) NOT NULL,

    industry VARCHAR(100) NOT NULL,

    company_size VARCHAR(30),

    headquarters VARCHAR(100),

    website TEXT,

    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_company
        PRIMARY KEY (company_id),

    CONSTRAINT uq_company_name
        UNIQUE (company_name),

    CONSTRAINT chk_company_status
        CHECK (status IN ('ACTIVE', 'INACTIVE'))
);