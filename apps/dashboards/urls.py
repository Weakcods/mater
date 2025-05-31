from django.urls import path
from .views import DashboardsView

urlpatterns = [
    path(
        "",
        DashboardsView.as_view(template_name="dashboard_analytics.html"),
        name="index",
    ),
    path(
        "new/",
        DashboardsView.as_view(template_name="dashboard_new_analytics.html"),
        name="new_analytics",
    )
]
