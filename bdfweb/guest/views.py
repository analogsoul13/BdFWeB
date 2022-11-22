from django.shortcuts import render
from user.models import ReqBlood
from user.models import User
from department.models import Department
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'home.html')

# Search using pin code - completed
def search(request):
    searchpin = request.GET.get("search")
    department = Department.objects.filter(Q(deppin=searchpin) & Q(status="approved"))
    return render(request, 'search_results.html', locals())

def blood_banks(request):
    department = Department.objects.filter(status="approved")
    return render(request, 'blood_banks.html', locals())

def donate(request):
    return render(request, 'donate_fund.html')

def guest_donate_blood(request):
    reqblood = ReqBlood.objects.all
    return render(request, 'donate_blood.html', locals())

def about(request):
    return render(request, 'about_us.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def contribute(request):
    return render(request, 'contribute_fund.html')