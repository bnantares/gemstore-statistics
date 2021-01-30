from django.shortcuts import render
from django.views.generic import View
from django.db import models
from django.db import connection
from .models import *
from django.db.models import Sum

# Create your views here.

class ToplistCustomers(models.Manager, View):
    def get(self, request):

        LIMIT = 5
        top_customers_list = list(Sale.objects.values('customer').annotate(spent_money=Sum('total')).order_by('-spent_money'))[:LIMIT]
        all_data = Sale.objects.values('customer', 'total', 'item').filter(customer__in=[a['customer'] for a in top_customers_list])
        unique = []
        for x in top_customers_list:
            x['gems'] = list(set([y['item'] for y in all_data if (x['customer'] == y['customer'])]))
            unique.extend(x['gems'])       
        for x in top_customers_list:
            for y in list(x['gems']):
                if unique.count(y) == 1: x['gems'].remove(y)

        for sale in Sale.objects.all():
            sale.delete()

        return render(request, 'sales/top_customers.html', context={'top_customers': top_customers_list})