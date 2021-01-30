from django.urls import path
from .views import *

app_name = 'top_customers'

urlpatterns = [
    path('', ToplistCustomers.as_view(), name='top_customers_url')
]