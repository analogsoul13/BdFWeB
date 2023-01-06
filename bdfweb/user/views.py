from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from department.models import Department
from django.db.models import Q
from django.core.paginator import Paginator





# Create your views here.
# otp login not implemented
def user_otp_login(request):
    return render(request, 'user_login.html')


# verify otp not implemented
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


# user search function
def user_search(request):
    if not request.user.is_authenticated:
        return redirect('register')
    searchpin = request.GET.get("search")
    try:
        department = Department.objects.filter(Q(deppin=searchpin) & Q(status="approved"))
        error = "no"
    except:
        error = "yes"
    return render(request, 'user_search_results.html', locals())


# donate blood after user logged in
def donate_blood(request):
    if not request.user.is_authenticated:
        return redirect('register')
    user = request.user
    donor = Donor.objects.get(user=user)
    reqblood = ReqBlood.objects.all()
    paginator = Paginator(reqblood,6)
    page_number = request.GET.get('page')
    reqbloodfinaldata = paginator.get_page(page_number)
    totalpage = reqbloodfinaldata.paginator.num_pages
    totalPagelist = [n+1 for n in range(totalpage)]
    return render(request, 'user_donate_blood.html',locals())



# help fundraising after user logged in + Pagination
def help_fundraising(request):
    if not request.user.is_authenticated:
        return redirect('register')
    fundraisers = ReqCampaign.objects.filter(Q(status="approved") & Q(depstatus="approved"))
    paginator = Paginator(fundraisers,3)
    page_number = request.GET.get('page')
    fundraiserfinaldata = paginator.get_page(page_number)
    totalpage = fundraiserfinaldata.paginator.num_pages
    totalPagelist = [n+1 for n in range(totalpage)]
    return render(request, 'user_donate_fund.html', locals())


# bloodbanks display page after user logged in
def user_bloodbanks(request):
    if not request.user.is_authenticated:
        return redirect('register')
    department = Department.objects.filter(status="approved")
    paginator = Paginator(department,6)
    page_number = request.GET.get('page')
    departmentfinaldata = paginator.get_page(page_number)
    totalpage = departmentfinaldata.paginator.num_pages
    totalPagelist = [n+1 for n in range(totalpage)]

    return render(request, 'user_blood_banks.html', locals())



# user logout
def Logout(request):
    logout(request)
    return redirect ('home')


# user dashboard
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


# user profile page and edit details
def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('register')
    error = ""  # for alert
    user = request.user
    donor = Donor.objects.get(user=user)
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
    return render(request, 'user_profile.html',locals())

# Be A Donor
def be_a_donor(request):
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request, 'user_be_donor.html')


# User Making an appointment for be regular a donor
def make_appointment(request):
    if not request.user.is_authenticated:
        return redirect('register')
    searchpin = request.GET.get("search")
    department = Department.objects.filter(Q(deppin=searchpin) & Q(status="approved"))
    user = request.user
    donor = Donor.objects.get(user=user)
    pin = {'searchpin' : searchpin}
    if request.method=="POST":
        dfname = request.POST.get('donorfname')
        dlname = request.POST.get('donorlname')
        dage = request.POST.get('donorage')
        dplace = request.POST.get('donorplace')
        dpin = request.POST.get('donorpin')
        dmob = request.POST.get('donormob')
        dbloodgroup = request.POST.get('donorbloodgroup')
        dbloodbank = request.POST.get('donorbloodbank')
        dappointmentdate = request.POST.get('donorappointmentdate')
        rdonor = request.POST.get('regulardonorornot')
        try:
            DonorAppointment.objects.create(user=donor, fname=dfname, lname=dlname, age=dage, place=dplace, pin=dpin, mob=dmob, bloodgroup=dbloodgroup, bloodbank=dbloodbank, appointmentdate=dappointmentdate, regulardonor=rdonor, status="pending")
            error = "no"
        except:
            error = "yes"
    return render(request, 'user_make_appointment.html',locals())

# User Reqesting an appointment ffrom bloodbanks page
def request_appointment(request, pid):
    if not request.user.is_authenticated:
        return redirect('register')
    department = Department.objects.get(id=pid)
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
        dbloodbank = request.POST.get('donorbloodbank')
        dappointmentdate = request.POST.get('donorappointmentdate')
        rdonor = request.POST.get('regulardonorornot')
        try:
            DonorAppointment.objects.create(user=donor, fname=dfname, lname=dlname, age=dage, place=dplace, pin=dpin, mob=dmob, bloodgroup=dbloodgroup, bloodbank=dbloodbank, appointmentdate=dappointmentdate, regulardonor=rdonor, status="pending")
            error = "no"
        except:
            error = "yes"
    return render(request, 'user_request_appointment.html',locals())


# View appointments - need to display department name to visit
def view_appointments(request):
    if not request.user.is_authenticated:
        return redirect('register')
    user = request.user
    donor = Donor.objects.get(user=user)
    #bloodbank = DonorAppointment.objects.get(user=user )
    appointment = DonorAppointment.objects.filter(user=donor)
    #department = Department.objects.filter(Q(status="approved") & Q(user=donor))
    return render(request, 'user_view_appointments.html', locals())


# User Requesting a campaign for patient to hospital
def request_campaign(request):
    if not request.user.is_authenticated:
        return redirect('register')
    if 'term' in request.GET:
        qs = Department.objects.filter(depname__icontains=request.GET.get('term'))
        departments = list()
        for department in qs:
            departments.append(Department.depname)
        return JsonResponse(departments, safe=False)
    user = request.user
    donor = Donor.objects.get(user=user)
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




