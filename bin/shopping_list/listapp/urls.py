from django.urls import path
from . import views

app_name = 'listapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('location/', views.LocationView.as_view(), name='location'),
    path('list-display/', views.ListDisplayView.as_view(), name='list_display'),
    path('list-create/', views.ListCreateView.as_view(), name='list_create'),
    path('list-delete/<int:pk>/', views.ListDeleteView.as_view(), name='list_delete'),
]

