CREATE TABLE core.application_status_history (

    history_id BIGSERIAL,

    application_id BIGINT NOT NULL,

    previous_status VARCHAR(20),

    new_status VARCHAR(20) NOT NULL,

    changed_by VARCHAR(100) NOT NULL,

    changed_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    remarks TEXT,

    CONSTRAINT pk_application_status_history
        PRIMARY KEY (history_id),

    CONSTRAINT fk_application_history_application
        FOREIGN KEY (application_id)
        REFERENCES core.application(application_id)
        ON DELETE CASCADE,

    CONSTRAINT chk_previous_status
        CHECK (
            previous_status IS NULL OR
            previous_status IN (
                'APPLIED',
                'SCREENING',
                'INTERVIEW',
                'OFFERED',
                'HIRED',
                'REJECTED',
                'WITHDRAWN'
            )
        ),

    CONSTRAINT chk_new_status
        CHECK (
            new_status IN (
                'APPLIED',
                'SCREENING',
                'INTERVIEW',
                'OFFERED',
                'HIRED',
                'REJECTED',
                'WITHDRAWN'
            )
        )

);