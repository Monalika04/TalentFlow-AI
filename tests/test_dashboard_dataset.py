from analytics.services.dashboard_service import (
    DashboardService,
)

df = DashboardService.analytics()

print(df.head())

print()

print(df.info())