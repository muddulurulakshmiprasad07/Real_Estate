from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='user_logout'),

    path('property/<int:property_id>/',
         views.property_detail, name='property_detail'),

    path('buy/<int:property_id>/',
         views.buy_property, name='buy_property'),

    path('contact/<int:property_id>/',
         views.contact_owner, name='contact_owner'),
]