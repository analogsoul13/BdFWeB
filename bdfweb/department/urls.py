from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dep_login/', views.dep_login, name='dep_login'),
    path('dep_register/', views.dep_register, name='dep_register'),
    path('dep_home/', views.dep_home, name='dep_home'),
    path('dep_dashboard/', views.dep_dashboard, name='dep_dashboard'),
    path('dep_profile/', views.dep_profile, name='dep_profile'),
    path('donor_requests/', views.donor_requests, name='donor_requests'),
    path('actove_donors/', views.active_donors, name='active_donors'),
    path('view_donor_details/<int:pid>', views.donor_details, name='donor_details'),
    path('scheduled_appointments/', views.scheduled_appointments, name='scheduled_appointments'),
    path('create_fundraiser/', views.create_fundraiser, name='create_fundraiser'),
    path('view_fundraiser/', views.view_fundraiser, name='view_fundraiser'),
    path('verify_fundraiser/<int:pid>', views.verify_fundraiser, name='verify_fundraiser'),
    path('logout/', views.Logout, name='dep_logout'),

    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
