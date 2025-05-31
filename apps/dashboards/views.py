from django.views.generic import TemplateView
from web_project import TemplateLayout
from .models import SalesData, Transaction, WeeklyOverview, CountryStats
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
