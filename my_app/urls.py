from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('new_search/', views.new_search, name='new_search')
]