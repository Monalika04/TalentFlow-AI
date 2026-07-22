CREATE TABLE core.job (

    job_id BIGSERIAL,

    company_id BIGINT NOT NULL,

    job_title VARCHAR(150) NOT NULL,

    department VARCHAR(100) NOT NULL,

    job_description TEXT NOT NULL,

    location VARCHAR(100) NOT NULL,

    employment_type VARCHAR(30) NOT NULL,

    min_experience NUMERIC(4,1) NOT NULL,

    max_experience NUMERIC(4,1) NOT NULL,

    min_salary NUMERIC(12,2) NOT NULL,

    max_salary NUMERIC(12,2) NOT NULL,

    vacancies INTEGER NOT NULL DEFAULT 1,

    status VARCHAR(20) NOT NULL DEFAULT 'OPEN',

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_job
        PRIMARY KEY (job_id),

    CONSTRAINT fk_job_company
        FOREIGN KEY (company_id)
        REFERENCES core.company(company_id),

    CONSTRAINT chk_job_experience
        CHECK (min_experience >= 0
        AND max_experience >= min_experience),

    CONSTRAINT chk_job_salary
        CHECK (min_salary >= 0
        AND max_salary >= min_salary),

    CONSTRAINT chk_job_vacancies
        CHECK (vacancies > 0),

    CONSTRAINT chk_job_employment
        CHECK (employment_type IN
        (
            'FULL_TIME',
            'PART_TIME',
            'CONTRACT',
            'INTERNSHIP'
        )),

    CONSTRAINT chk_job_status
        CHECK (status IN
        (
            'OPEN',
            'CLOSED',
            'ON_HOLD',
            'CANCELLED'
        ))

);