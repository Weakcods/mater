from django.contrib import admin
from .models import SalesData, Transaction, WeeklyOverview, CountryStats

@admin.register(SalesData)
class SalesDataAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'target')
    list_filter = ('date',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'type', 'amount', 'description')
    list_filter = ('type', 'date')
    search_fields = ('description',)

@admin.register(WeeklyOverview)
class WeeklyOverviewAdmin(admin.ModelAdmin):
    list_display = ('week_start', 'total_sales', 'total_orders', 'growth_rate')
    list_filter = ('week_start',)

@admin.register(CountryStats)
class CountryStatsAdmin(admin.ModelAdmin):
    list_display = ('country', 'sales', 'growth_rate', 'last_update')
    list_filter = ('country', 'last_update')
    search_fields = ('country',)
