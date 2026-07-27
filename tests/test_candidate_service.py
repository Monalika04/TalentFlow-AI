from analytics.services.candidate_service import CandidateService

service = CandidateService()

dashboard = service.get_candidate_dashboard()

for key, value in dashboard.items():

    print()

    print("=" * 80)

    print(key.upper())

    print("=" * 80)

    print(value)