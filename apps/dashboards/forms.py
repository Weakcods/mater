from django import forms
from .models import SalesData, Transaction, WeeklyOverview, CountryStats

class SalesDataForm(forms.ModelForm):
    class Meta:
        model = SalesData
        fields = ['date', 'amount', 'target']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'YYYY-MM-DD',
                }
            ),
            'amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter amount',
                    'step': '0.01'
                }
            ),
            'target': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter target',
                    'step': '0.01'
                }
            ),
        }
        labels = {
            'date': 'Sales Date',
            'amount': 'Sales Amount',
            'target': 'Target Amount'
        }
        help_texts = {
            'amount': 'Enter the actual sales amount for this date',
            'target': 'Enter the target sales amount for this date'
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'type', 'amount', 'description']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WeeklyOverviewForm(forms.ModelForm):
    class Meta:
        model = WeeklyOverview
        fields = ['week_start', 'total_sales', 'total_orders', 'growth_rate']
        widgets = {
            'week_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'total_sales': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_orders': forms.NumberInput(attrs={'class': 'form-control'}),
            'growth_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CountryStatsForm(forms.ModelForm):
    class Meta:
        model = CountryStats
        fields = ['country', 'sales', 'growth_rate']
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'sales': forms.NumberInput(attrs={'class': 'form-control'}),
            'growth_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }
