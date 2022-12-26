from django.shortcuts import render
from user.models import ReqBlood
from user.models import ReqCampaign
from user.models import User
from department.models import Department
from django.db.models import Q
from django.core.paginator import Paginator

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
    paginator = Paginator(department,6)
    page_number = request.GET.get('page')
    departmentfinaldata = paginator.get_page(page_number)
    totalpage = departmentfinaldata.paginator.num_pages
    totalPagelist = [n+1 for n in range(totalpage)]
    return render(request, 'blood_banks.html', locals())


def donate(request):
    fundraisers = ReqCampaign.objects.filter(Q(status="approved") & Q(depstatus="approved"))
    paginator = Paginator(fundraisers,3)
    page_number = request.GET.get('page')
    fundraiserfinaldata = paginator.get_page(page_number)
    totalpage = fundraiserfinaldata.paginator.num_pages
    totalPagelist = [n+1 for n in range(totalpage)]
    return render(request, 'donate_fund.html', locals())


def guest_donate_blood(request):
    reqblood = ReqBlood.objects.all()
    paginator = Paginator(reqblood,6)
    page_number = request.GET.get('page')
    reqbloodfinaldata = paginator.get_page(page_number)
    totalpage = reqbloodfinaldata.paginator.num_pages
    totalPagelist = [n+1 for n in range(totalpage)]
    return render(request, 'donate_blood.html', locals())


def about(request):
    return render(request, 'about_us.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def contribute(request):
    return render(request, 'contribute_fund.html')
    