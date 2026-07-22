CREATE TABLE core.resume (

    resume_id BIGSERIAL,

    candidate_id BIGINT NOT NULL,

    file_name VARCHAR(255) NOT NULL,

    file_path TEXT NOT NULL,

    file_type VARCHAR(20) NOT NULL,

    file_size_kb NUMERIC(10,2) NOT NULL,

    resume_version INTEGER NOT NULL DEFAULT 1,

    upload_date TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    parsing_status VARCHAR(20) NOT NULL DEFAULT 'PENDING',

    ai_summary TEXT,

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_resume
        PRIMARY KEY (resume_id),

    CONSTRAINT fk_resume_candidate
        FOREIGN KEY (candidate_id)
        REFERENCES core.candidate(candidate_id),

    CONSTRAINT chk_resume_file_type
        CHECK (file_type IN ('PDF', 'DOCX')),

    CONSTRAINT chk_resume_status
        CHECK (parsing_status IN (
            'PENDING',
            'PROCESSING',
            'COMPLETED',
            'FAILED'
        )),

    CONSTRAINT chk_resume_version
        CHECK (resume_version >= 1),

    CONSTRAINT chk_resume_size
        CHECK (file_size_kb > 0)

);