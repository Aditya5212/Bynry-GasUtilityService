from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user,name='logout'),
    path('register/', views.register_user, name='register'),
    path('cust_req/', views.submit_request, name='customer_request'),
    path('track_requests/', views.track_requests, name='track_requests'),
    path('modify_request/<int:request_id>/', views.modify_request, name='modify_request'),
    path('delete_request/<int:request_id>', views.delete_request, name='delete_request'),
]