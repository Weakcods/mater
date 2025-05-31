from django.urls import path
from .views import (
    DashboardsView,
    SalesDataListView, SalesDataCreateView, SalesDataUpdateView, SalesDataDeleteView,
    TransactionListView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView,
    WeeklyOverviewListView, WeeklyOverviewCreateView, WeeklyOverviewUpdateView, WeeklyOverviewDeleteView,
    CountryStatsListView, CountryStatsCreateView, CountryStatsUpdateView, CountryStatsDeleteView,
)

app_name = 'dashboards'

urlpatterns = [
    path("", DashboardsView.as_view(template_name="dashboard_analytics.html"), name="index"),
    path("new/", DashboardsView.as_view(template_name="dashboard_new_analytics.html"), name="new_analytics"),
    
    # Sales Data URLs
    path("sales/", SalesDataListView.as_view(), name="sales_list"),
    path("sales/create/", SalesDataCreateView.as_view(), name="sales_create"),
    path("sales/<int:pk>/update/", SalesDataUpdateView.as_view(), name="sales_update"),
    path("sales/<int:pk>/delete/", SalesDataDeleteView.as_view(), name="sales_delete"),
    
    # Transaction URLs
    path("transactions/", TransactionListView.as_view(), name="transaction_list"),
    path("transactions/create/", TransactionCreateView.as_view(), name="transaction_create"),
    path("transactions/<int:pk>/update/", TransactionUpdateView.as_view(), name="transaction_update"),
    path("transactions/<int:pk>/delete/", TransactionDeleteView.as_view(), name="transaction_delete"),
    
    # Weekly Overview URLs
    path("weekly/", WeeklyOverviewListView.as_view(), name="weekly_list"),
    path("weekly/create/", WeeklyOverviewCreateView.as_view(), name="weekly_create"),
    path("weekly/<int:pk>/update/", WeeklyOverviewUpdateView.as_view(), name="weekly_update"),
    path("weekly/<int:pk>/delete/", WeeklyOverviewDeleteView.as_view(), name="weekly_delete"),
    
    # Country Stats URLs
    path("countries/", CountryStatsListView.as_view(), name="country_list"),
    path("countries/create/", CountryStatsCreateView.as_view(), name="country_create"),
    path("countries/<int:pk>/update/", CountryStatsUpdateView.as_view(), name="country_update"),
    path("countries/<int:pk>/delete/", CountryStatsDeleteView.as_view(), name="country_delete"),
]
