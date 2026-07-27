from analytics.services.executive_service import ExecutiveService

service = ExecutiveService()

print()

print("=" * 70)
print("EXECUTIVE METRICS")
print("=" * 70)

print(service.get_dashboard_metrics())

print()

print("=" * 70)
print("APPLICATION STATUS")
print("=" * 70)

print(service.get_application_status())

print()

print("=" * 70)
print("JOBS BY DEPARTMENT")
print("=" * 70)

print(service.get_jobs_by_department())

print()

print("=" * 70)
print("COMPANIES BY INDUSTRY")
print("=" * 70)

print(service.get_companies_by_industry())