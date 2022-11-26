from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('user_created_posts/', views.user_created_posts, name='user_created_posts'),
    path('all_users/', views.all_users, name='all_users'),
    path('verified_donors/', views.verified_donors, name='verified_donors'),
    path('view_user_details/<int:pid>', views.user_details, name='view_user_details'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('delete_donor/<int:pid>', views.admin_delete_donor, name='delete_donor'),
    path('department_requests', views.dep_requests, name='dep_requests'),
    path('approved_requests', views.approved_requests, name='approved_requests'),
    path('rejected_requests', views.rejected_requests, name='rejected_requests'),
    path('view_all_departments', views.view_all_dep, name='view_all_dep'),
    path('view_department_details/<int:pid>', views.dep_details, name='dep_details'),
    path('delete_department/<int:pid>', views.delete_dep, name='delete_dep'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)