from django.urls import path
from . import views

app_name = 'icecream'

urlpatterns = [
    path('daily/', views.daily, name='daily'),
    path('weekly/', views.weekly, name='weekly'),
    path('seasonal/', views.seasonal, name='seasonal'),
    path('new/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    # path('<int:pk>/delete/', views.delete_view, name='delete'),
    path("", views.index, name='index'),
    path('<int:pk>/likes', views.likes, name='likes'),
]
