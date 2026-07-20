CREATE TABLE core.company (

    company_id BIGSERIAL PRIMARY KEY,

    company_name VARCHAR(150) NOT NULL UNIQUE,

    industry VARCHAR(100) NOT NULL,

    company_size VARCHAR(30),

    headquarters VARCHAR(100),

    website TEXT,

    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_company_status
        CHECK (status IN ('ACTIVE', 'INACTIVE'))

);


