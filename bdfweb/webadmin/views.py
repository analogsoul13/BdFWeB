from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from user.models import ReqBlood
from user.models import Donor
from user.models import User
from user.models import DonorAppointment
from department.models import Department
from datetime import datetime
from django.db.models import Q, Count
# Create your views here.
# login and authentication of admin
def admin_login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
        
    return render(request, 'admin_login.html', locals())


# admin home page after succesful login
def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    total_requests = Department.objects.count()
    total_users = Donor.objects.count()
    total_departments = Department.objects.filter(status="approved")
    departments = total_departments.count()
    total = {'total_requests' :total_requests ,'total_users' :total_users , 'total_departments' :total_departments, 'departments' :departments}
    return render(request, 'admin_home.html', total)


# Display All posts created by users   
def user_created_posts(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = request.user
    reqblood = ReqBlood.objects.all
    return render(request, 'admin_user_created_posts.html',locals())


# Display All Users   
def all_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.all
    return render(request, 'admin_all_users.html',locals())


# Display All Verified Regular Donors  
def verified_donors(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donors = DonorAppointment.objects.all
    return render(request, 'admin_verified_donors.html',locals())


# View User Details   
def user_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.get(id=pid)
    return render(request, 'admin_view_user_details.html',locals())


# ADMIN Profile   
def admin_profile(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_profile.html')


# Delete User Details delete also from user model (parent)  
def admin_delete_donor(request,pid):
    User.objects.get(id=pid).delete()
    return redirect('all_users')


# Display all request from departments
def dep_requests(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    department = Department.objects.filter(status="pending")
    return render(request, 'admin_dep_requests.html', locals())


# Display all approved departments
def approved_requests(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    department = Department.objects.filter(status="approved")
    return render(request, 'admin_approved_requests.html', locals())


# Display all Rejected departments
def rejected_requests(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    department = Department.objects.filter(status="rejected")
    return render(request, 'admin_rejected_requests.html', locals())


# Display all departments both rejected and accepted
def view_all_dep(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    department = Department.objects.all()
    return render(request, 'admin_all_departments.html', locals())


# View Department Details   
def dep_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    department = Department.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST.get('status')
        adminremark = request.POST.get('remark')
        try:
            department.adminremark = adminremark
            department.status = status
            department.updationdate = datetime.now()
            department.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin_view_dep_details.html',locals())


# Delete Department Details delete also from user model (parent)  
def delete_dep(request,pid):
    Department.objects.get(id=pid).delete()
    return redirect('view_all_dep')


# Admin logout
def Logout(request):
    logout(request)
    return redirect ('admin_home')



