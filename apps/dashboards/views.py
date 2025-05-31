from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from web_project import TemplateLayout
from .models import SalesData, Transaction, WeeklyOverview, CountryStats
from .forms import SalesDataForm, TransactionForm, WeeklyOverviewForm, CountryStatsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to dashboards/urls.py file for more pages.
"""


class DashboardsView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Get latest sales data
        latest_sales = SalesData.objects.order_by('-date').first()

        # Get recent transactions
        recent_transactions = Transaction.objects.all()[:5]

        # Get weekly overview
        current_week = WeeklyOverview.objects.order_by('-week_start').first()

        # Get top countries by sales
        top_countries = CountryStats.objects.order_by('-sales')[:5]

        # Calculate monthly growth
        thirty_days_ago = timezone.now() - timedelta(days=30)
        monthly_transactions = Transaction.objects.filter(
            date__gte=thirty_days_ago
        ).aggregate(total=Sum('amount'))

        context.update(
            {
                'latest_sales': latest_sales,
                'recent_transactions': recent_transactions,
                'weekly_overview': current_week,
                'top_countries': top_countries,
                'monthly_growth': monthly_transactions.get('total', 0),
            }
        )

        return context

# Sales Data CRUD Views
class SalesDataListView(LoginRequiredMixin, ListView):
    model = SalesData
    template_name = 'dashboard_crud/sales_list.html'
    context_object_name = 'sales_data'
    ordering = ['-date']

class SalesDataCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SalesData
    form_class = SalesDataForm
    template_name = 'dashboard_crud/sales_form.html'
    success_url = reverse_lazy('dashboards:sales_list')
    success_message = "Sales data was created successfully"

class SalesDataUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SalesData
    form_class = SalesDataForm
    template_name = 'dashboard_crud/sales_form.html'
    success_url = reverse_lazy('dashboards:sales_list')
    success_message = "Sales data was updated successfully"

class SalesDataDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SalesData
    template_name = 'dashboard_crud/sales_confirm_delete.html'
    success_url = reverse_lazy('dashboards:sales_list')
    success_message = "Sales data was deleted successfully"

# Transaction CRUD Views
class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'dashboard_crud/transaction_list.html'
    context_object_name = 'transactions'
    ordering = ['-date']

class TransactionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'dashboard_crud/transaction_form.html'
    success_url = reverse_lazy('dashboards:transaction_list')
    success_message = "Transaction was created successfully"

class TransactionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'dashboard_crud/transaction_form.html'
    success_url = reverse_lazy('dashboards:transaction_list')
    success_message = "Transaction was updated successfully"

class TransactionDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Transaction
    template_name = 'dashboard_crud/transaction_confirm_delete.html'
    success_url = reverse_lazy('dashboards:transaction_list')
    success_message = "Transaction was deleted successfully"

# Weekly Overview CRUD Views
class WeeklyOverviewListView(LoginRequiredMixin, ListView):
    model = WeeklyOverview
    template_name = 'dashboard_crud/weekly_list.html'
    context_object_name = 'weekly_data'
    ordering = ['-week_start']

class WeeklyOverviewCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = WeeklyOverview
    form_class = WeeklyOverviewForm
    template_name = 'dashboard_crud/weekly_form.html'
    success_url = reverse_lazy('dashboards:weekly_list')
    success_message = "Weekly overview was created successfully"

class WeeklyOverviewUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = WeeklyOverview
    form_class = WeeklyOverviewForm
    template_name = 'dashboard_crud/weekly_form.html'
    success_url = reverse_lazy('dashboards:weekly_list')
    success_message = "Weekly overview was updated successfully"

class WeeklyOverviewDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = WeeklyOverview
    template_name = 'dashboard_crud/weekly_confirm_delete.html'
    success_url = reverse_lazy('dashboards:weekly_list')
    success_message = "Weekly overview was deleted successfully"

# Country Stats CRUD Views
class CountryStatsListView(LoginRequiredMixin, ListView):
    model = CountryStats
    template_name = 'dashboard_crud/country_list.html'
    context_object_name = 'country_stats'
    ordering = ['-sales']

class CountryStatsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CountryStats
    form_class = CountryStatsForm
    template_name = 'dashboard_crud/country_form.html'
    success_url = reverse_lazy('dashboards:country_list')
    success_message = "Country stats were created successfully"

class CountryStatsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CountryStats
    form_class = CountryStatsForm
    template_name = 'dashboard_crud/country_form.html'
    success_url = reverse_lazy('dashboards:country_list')
    success_message = "Country stats were updated successfully"

class CountryStatsDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CountryStats
    template_name = 'dashboard_crud/country_confirm_delete.html'
    success_url = reverse_lazy('dashboards:country_list')
    success_message = "Country stats were deleted successfully"
