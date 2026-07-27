from analytics.services.job_service import JobService

service = JobService()

dashboard = service.get_job_dashboard()

for key, value in dashboard.items():

    print()

    print("=" * 80)

    print(key.upper())

    print("=" * 80)

    print(value)