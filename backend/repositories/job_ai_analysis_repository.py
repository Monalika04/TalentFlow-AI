from backend.models.job_ai_analysis_model import (
    JobAIAnalysis,
    JobAIAnalysisStatus,
)


class JobAIAnalysisRepository:

    def __init__(self, db):
        self.db = db

    def create_new_version(
        self,
        job_id: int,
        model_name: str,
        prompt_version: str,
    ):

        latest = (
            self.db.query(JobAIAnalysis)
            .filter(JobAIAnalysis.job_id == job_id)
            .order_by(
                JobAIAnalysis.analysis_version.desc()
            )
            .first()
        )

        version = (
            latest.analysis_version + 1
            if latest
            else 1
        )

        analysis = JobAIAnalysis(
            job_id=job_id,
            model_name=model_name,
            prompt_version=prompt_version,
            analysis_version=version,
            status=JobAIAnalysisStatus.PENDING,
        )

        self.db.add(analysis)
        self.db.flush()

        return analysis

    def update_status(
        self,
        analysis: JobAIAnalysis,
        status: JobAIAnalysisStatus,
    ):

        analysis.status = status

    def save_raw_text(
        self,
        analysis: JobAIAnalysis,
        raw_job_text: str,
    ):

        analysis.raw_job_text = raw_job_text

    def save_ai_response(
        self,
        analysis: JobAIAnalysis,
        response_json: dict,
        execution_time_ms: float,
    ):

        analysis.ai_response_json = response_json
        analysis.execution_time_ms = execution_time_ms

    def mark_failed(
        self,
        analysis: JobAIAnalysis,
        error: str,
    ):

        analysis.status = JobAIAnalysisStatus.FAILED
        analysis.error_message = error

    def get_latest_by_job(
        self,
        job_id: int,
    ):

        return (
            self.db.query(JobAIAnalysis)
            .filter(JobAIAnalysis.job_id == job_id)
            .order_by(
                JobAIAnalysis.analysis_version.desc()
            )
            .first()
        )

    def get_by_analysis_id(
        self,
        analysis_id: int,
    ):

        return (
            self.db.query(JobAIAnalysis)
            .filter(
                JobAIAnalysis.analysis_id == analysis_id
            )
            .first()
        )
        
    def get_latest_by_job_id(
        self,
        job_id: int,
    ):

        return (
            self.db.query(JobAIAnalysis)
            .filter(
                JobAIAnalysis.job_id == job_id
            )
            .order_by(
                JobAIAnalysis.analysis_version.desc()
            )
            .first()
        )