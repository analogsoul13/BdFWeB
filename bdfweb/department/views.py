from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from user.models import DonorAppointment, Donor, ReqCampaign
from datetime import datetime
from django.db.models import Q




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
    user = request.user
    department = Department.objects.get(user=user)
    try:
        appointment = DonorAppointment.objects.filter(Q(status="pending") & Q(bloodbank=department))
        error = "no"
    except:
        error = "yes"
          
    return render(request, 'dep_donor_requests.html', locals())


# View Donor Appointment Requests and take action
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



# Department Can Request Fundraisers to Admin
def create_fundraiser(request):
    if not request.user.is_authenticated:
        return redirect('dep_login')
    user = request.user
    department = Department.objects.get(user=user)
    if request.method=="POST":
        pfname = request.POST.get('patientfname')
        plname = request.POST.get('patientlname')
        page = request.POST.get('patientage')
        pplace = request.POST.get('patientplace')
        ppin = request.POST.get('patientpin')
        pmob = request.POST.get('patientmob')
        pamount = request.POST.get('patientamount')
        pdescription = request.POST.get('patientdescription')
        phospital = request.POST.get('patienthospital')
        pdocumentpic = request.FILES.get('patientmedicaldocpic')
        ppic = request.FILES.get('patientpic')
        try:
            ReqCampaign.objects.create(user=department, fname=pfname, lname=plname, age=page, place=pplace, pin=ppin, mob=pmob, amount=pamount, description=pdescription, hospital=phospital, documentpic=pdocumentpic, patientpic=ppic, status="pending")
            error="no"
        except:
            error="yes"
    return render(request, 'dep_create_fundraiser.html', locals())


# View Fundraiser Requests from user
def view_fundraiser(request):
    fundraiser = ReqCampaign.objects.filter(status = "pending")
    return render(request, 'dep_view_fundraisers.html', locals())


# Verify and set department remark for fundraiser requested by user
def verify_fundraiser(request,pid):
    if not request.user.is_authenticated:
        return redirect('dep_login')
    fundraiser = ReqCampaign.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST.get('fundraiserstatus')
        depremark = request.POST.get('departmentremark')
        try:
            fundraiser.departmentremark = depremark
            fundraiser.status = status
            fundraiser.updationdate = datetime.now()
            fundraiser.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'dep_verify_fundraiser.html', locals())


def dep_dashboard(request):
    donors = DonorAppointment.objects.count()
    data ={'donors' : donors}
    return render(request, 'dep_dashboard.html', data)


def dep_profile(request):
    return render(request, 'dep_profile.html')


def Logout(request):
    logout(request)
    return redirect ('home')
