from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
    
urlpatterns = [
    
    path('register/', views.user_otp_login, name='register'),
    path('login_with_password/', views.user_pwd_login, name='upwd_login'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('user_details/', views.user_register, name='u_form'),
    path('user_home/', views.user_home, name='user_home'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('logout/', views.Logout, name='logout'),
    path('donate_blood/', views.donate_blood, name='donate_blood'),
    path('help_fundraising/', views.help_fundraising, name='help_fundraising'),
    path('user_blood_banks/', views.user_bloodbanks, name='user_bloodbanks'),
    path('user_request_blood/', views.user_request_blood, name='user_request_blood'),
    path('user_post_details/', views.post_details, name='post_details'),
    path('be_a_donor/', views.be_a_donor, name='be_a_donor'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),
    path('request_a_campaign/', views.request_campaign, name='request_campaign'),
    path('view_campaigns/', views.view_campaigns, name='view_campaigns'),
    path('about_us/', views.about_us, name='user_about_us'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)