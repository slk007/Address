from django.urls import path
from .views import home, add_address

urlpatterns = [
    path('', home, name='home'),
    path('add_address/', add_address, name='add_address')
]