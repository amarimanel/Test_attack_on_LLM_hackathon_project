from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                      # Doit être views.home
    path('test/', views.test_page, name='test'),           # Doit être views.test_page
    path('stats/', views.stats_page, name='stats'),         # Doit être views.stats_page
    path('dashboard/', views.dashboard_view, name='dashboard'), # Doit être views.dashboard_view


    path('download/<str:format_type>/', views.download_dataset, name='download_dataset'),

]