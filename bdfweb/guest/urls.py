from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('blood_banks/', views.blood_banks, name='blood_banks'),
    path('donate/', views.donate, name='donate'),
    path('urgently_needed/', views.guest_donate_blood, name='guest_view_posts'),
    path('about/', views.about, name='about_us'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contribute_fund', views.contribute, name='contribute'),

]