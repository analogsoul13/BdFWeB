from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from user.models import DonorAppointment, Donor
from datetime import datetime




# Create your views here.
# department login only if admin approved
def dep_login(request):
    if request.method == "POST":
        u = request.POST.get('emailid')
        p = request.POST.get('pwd')
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Department.objects.get(user=user) # comparing user objects
                if user1.status != "pending":  #checking status is pending or not                 
                    login(request, user)
                    error = "no"
                else:
                    error = "not" 

            except:
                error = "yes"
        else:
            error = "yes"
    return render(request, 'dep_login.html', locals())


# registering department and receiving data from form
def dep_register(request):
    error = ""

    if request.method=='POST':
        dfname = request.POST.get('depfname')
        dlname = request.POST.get('deplname')
        dmob = request.POST.get('depmob')       
        dpin = request.POST.get('deppin')
        demail = request.POST.get('depmail')
        daddress = request.POST.get('depaddress')
        dpass = request.POST.get('pass')
        dpic = request.FILES.get('deppic')
        did = request.FILES.get('depidpic')
        dabout = request.POST.get('depabout')

        try:
            user = User.objects.create_user(first_name=dfname, last_name=dlname, username=demail, password=dpass)
            Department.objects.create(user=user, contact=dmob, address=daddress, deppic=dpic, deppin=dpin, depidpic=did, aboutdep=dabout, status="pending")
            error="no"

        except:
            error="yes"
       
    return render(request, 'dep_register.html', locals())


def dep_home(request):
    if not request.user.is_authenticated:
        return redirect('dep_login')
    return render(request, 'dep_home.html')


def donor_requests(request):
    if not request.user.is_authenticated:
        return redirect('dep_login')
    appointment = DonorAppointment.objects.filter(status="pending")
    return render(request, 'dep_donor_requests.html', locals())


def donor_details(request,pid):
    if not request.user.is_authenticated:
        return redirect('dep_login')
    donor = DonorAppointment.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST.get('appointmentstatus')
        depremark = request.POST.get('departmentremark')
        try:
            donor.departmentremark = depremark
            donor.status = status
            donor.updationdate = datetime.now()
            donor.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'dep_view_donor_details.html', locals())



# Department can view all approved upcoming appointments
def scheduled_appointments(request):
    if not request.user.is_authenticated:
        return redirect('dep_login')
    appointment = DonorAppointment.objects.filter(status="approved")
    return render(request, 'dep_scheduled_appointments.html', locals())



def create_fundraiser(request):
    if not request.user.is_authenticated:
        return redirect('dep_login')
    appointment = DonorAppointment.objects.filter(status="approved")
    return render(request, 'dep_create_fundraiser.html', locals())


def dep_dashboard(request):
    donors = DonorAppointment.objects.count()
    data ={'donors' : donors}
    return render(request, 'dep_dashboard.html', data)


def dep_profile(request):
    return render(request, 'dep_profile.html')


def Logout(request):
    logout(request)
    return redirect ('home')
