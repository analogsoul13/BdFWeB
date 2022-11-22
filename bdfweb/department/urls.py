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
    path('logout/', views.Logout, name='dep_logout'),

    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
