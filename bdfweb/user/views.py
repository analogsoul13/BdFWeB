from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from department.models import Department





# Create your views here.

def user_otp_login(request):
    return render(request, 'user_login.html')



def verify_otp(request):
    return render(request, 'verify_otp.html')
    

# User details adding to databse
def user_register(request):
    error = ""  # for alert

    if request.method == "POST":
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        uage = request.POST.get('userage')
        uplace = request.POST.get('userplace')
        upin = request.POST.get('userpincode')
        umob = request.POST.get('usermob')
        umail = request.POST.get('usermail')
        pwd = request.POST.get('userpass')
        ubgroup = request.POST.get('userbloodgroup')
        upic = request.FILES.get('userpic')
         
        try:
            user = User.objects.create_user(first_name=fname, last_name=lname, username=umail, password=pwd )
            Donor.objects.create(user=user, contact=umob, place=uplace, userpin=upin, userpic=upic, userbloodgroup=ubgroup, userdob=uage)
            error="no"

        except:
            error="yes"

    return render(request, 'user_register.html', locals())


# user login and checking details with database
def user_pwd_login(request):
    if request.method == "POST":
        uid = request.POST.get('uemailid')
        upass = request.POST.get('upassword')
        user = authenticate(username=uid, password=upass)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render (request, 'user_pswd_login.html',locals())




def user_home(request):
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request, 'user_home.html')


# donate blood after user logged in
def donate_blood(request):
    if not request.user.is_authenticated:
        return redirect('register')
    user = request.user
    donor = Donor.objects.get(user=user)
    reqblood = ReqBlood.objects.all()
    return render(request, 'user_donate_blood.html',locals())



# help fundraising after user logged in
def help_fundraising(request):
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request, 'user_donate_fund.html')


# bloodbanks display page after user logged in
def user_bloodbanks(request):
    if not request.user.is_authenticated:
        return redirect('register')
    department = Department.objects.filter(status="approved")
    return render(request, 'user_blood_banks.html', locals())



# user logout
def Logout(request):
    logout(request)
    return redirect ('home')



def user_dashboard(request):
    return render(request, 'user_dashboard.html')


# user creating a post requesting urgent blood donation for patient
def user_request_blood(request):
    if not request.user.is_authenticated:
        return redirect('register')
    user = request.user
    donor = Donor.objects.get(user=user)
    if request.method=="POST":
        reqfname = request.POST.get('reqfname')
        reqage = request.POST.get('reqage')
        reqplace = request.POST.get('reqplace')
        reqpin = request.POST.get('reqpin')
        reqmob = request.POST.get('reqmob')
        reqdescription = request.POST.get('reqdescription')
        reqbloodgroup = request.POST.get('reqbloodgroup')
        reqpic = request.FILES.get('reqpic')
        try:
            ReqBlood.objects.create(user=donor, fullname=reqfname, age=reqage, place=reqplace, pin=reqpin, mob=reqmob, description=reqdescription, bloodgroup=reqbloodgroup, pic=reqpic, status="pending")
            error="no"
        except:
            error="yes"


    return render(request, 'user_request_blood.html',locals())


# post details after user creating a post requesting blood
def post_details(request):
    if not request.user.is_authenticated:
        return redirect('register')
    user = request.user
    donor = Donor.objects.get(user=user)
    reqblood = ReqBlood.objects.filter(user=donor)
    return render(request, 'user_post_details.html',locals())


def user_profile(request):
    return render(request, 'user_profile.html')

# Be A Donor
def be_a_donor(request):
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request, 'user_be_donor.html')


# User Making an appointment for be regular a donor
def make_appointment(request):
    if not request.user.is_authenticated:
        return redirect('register')
    user = request.user
    donor = Donor.objects.get(user=user)
    if request.method=="POST":
        dfname = request.POST.get('donorfname')
        dlname = request.POST.get('donorlname')
        dage = request.POST.get('donorage')
        dplace = request.POST.get('donorplace')
        dpin = request.POST.get('donorpin')
        dmob = request.POST.get('donormob')
        dbloodgroup = request.POST.get('donorbloodgroup')
        dappointmentdate = request.POST.get('donorappointmentdate')
        rdonor = request.POST.get('regulardonorornot')
        try:
            DonorAppointment.objects.create(user=donor, fname=dfname, lname=dlname, age=dage, place=dplace, pin=dpin, mob=dmob, bloodgroup=dbloodgroup, appointmentdate=dappointmentdate, regulardonor=rdonor, status="pending")
            error = "no"
        except:
            error = "yes"
    return render(request, 'user_make_appointment.html', locals())


def view_appointments(request):
    if not request.user.is_authenticated:
        return redirect('register')
    user = request.user
    donor = Donor.objects.get(user=user)
    appointment = DonorAppointment.objects.filter(user=donor)
    return render(request, 'user_view_appointments.html', locals())


# User Requesting a campaign for patient to hospital
def request_campaign(request):
    if not request.user.is_authenticated:
        return redirect('register')
    user = request.user
    donor = Donor.objects.get(user=user)
    hospital = Department.objects.filter(status="approved")
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
        prwithpatient = request.POST.get('userrelationwithpatient')
        pdocumentpic = request.FILES.get('patientmedicaldocpic')
        ppic = request.FILES.get('patientpic')
        try:
            ReqCampaign.objects.create(user=donor, fname=pfname, lname=plname, age=page, place=pplace, pin=ppin, mob=pmob, amount=pamount, description=pdescription, hospital=phospital, rwithpatient=prwithpatient, documentpic=pdocumentpic, patientpic=ppic, status="pending")
            error="no"
        except:
            error="yes"
    return render(request, 'user_request_campaign.html')


# Display campaigns requested by user
def view_campaigns(request):
    if not request.user.is_authenticated:
        return redirect('register')
    user = request.user
    donor = Donor.objects.get(user=user)
    campaigns = ReqCampaign.objects.filter(user=donor)
    return render(request, 'user_view_campaigns.html', locals())


# User About Us
def about_us(request):
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request, 'user_about_us.html')




