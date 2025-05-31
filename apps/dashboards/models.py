from django.db import models
from django.utils import timezone

# Create your models here.
class SalesData(models.Model):
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    target = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        ordering = ['-date']
        
    def get_percentage(self):
        """Calculate percentage of target achieved"""
        if self.target and float(self.target) > 0:
            return (float(self.amount) / float(self.target)) * 100
        return 0
        
    def __str__(self):
        return f"{self.date} - ${self.amount}"

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
        ('transfer', 'Transfer'),
    )
    
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['-date']

class WeeklyOverview(models.Model):
    week_start = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_orders = models.IntegerField()
    growth_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage
    
    class Meta:
        ordering = ['-week_start']

class CountryStats(models.Model):
    country = models.CharField(max_length=100)
    sales = models.DecimalField(max_digits=10, decimal_places=2)
    growth_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage
    last_update = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Country stats"
