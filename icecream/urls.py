from django.urls import path
from . import views

app_name = 'icecream'

urlpatterns = [
    path('daily/', views.daily, name='daily'),
    path('weekly/', views.weekly, name='weekly'),
    path('seasonal/', views.seasonal, name='seasonal'),
    path("", views.index, name='index'),
]
