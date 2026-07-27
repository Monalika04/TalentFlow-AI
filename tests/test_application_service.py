from analytics.services.application_service import (
    ApplicationService,
)

service = ApplicationService()

dashboard = service.get_application_dashboard()

for key, value in dashboard.items():

    print()

    print("=" * 80)

    print(key.upper())

    print("=" * 80)

    print(value)