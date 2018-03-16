from django.shortcuts import render
from .models import Sign,Otp_match
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.http import HttpResponse,response
from django.http import JsonResponse
import random
from django.shortcuts import render_to_response
import json
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext


def p(request):
    return render(request,'index.html')

def signup(request):
    return render(request,
                  'signupajax.html',
                  )

@csrf_exempt
def validate_username(request):
    contxt={}
    if request.method=="POST":
        email = request.POST.get('email')
        fname =request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        contact=request.POST.get('contact')
        profile_picture=request.POST.get('profile_picture')
        print(profile_picture)
        emp = Sign.objects.create(fname=fname, lname=lname, username=uname, password=pwd, email=email,
                                  contact=contact, profile_picture=profile_picture)
        emp.save()

        otp2 = random.randrange(1000,9999)
        otp_save = Otp_match.objects.create(otp=otp2, user=emp)
        otp_save.save()

        # contxt['email']=email
        # contxt['fname']=fname
        # contxt['lname']=lname
        # contxt['uname']=uname
        # contxt['pwd']=pwd
        # contxt['contact']=contact
        # contxt['otp']=otp2
        # print(contxt)

        send_mail('OTP Email', 'your One Time Password is '+ str(otp2), 'shivam.mittal38@gmail.com', [email])


        request.session['email']=email
    return JsonResponse({"email":email,"success":True,"otp":otp2})

def Otp(request):
    return render(request,"otp.html")

# def Otp(request):
#     if request.method == "POST":
#         otp1 = request.POST.get("otp")
#         get_email=request.POST.get("email")
#
#         data=Otp_match.objects.get(email=get_email)
#         get_otp=data.otp
#         print(get_otp)
#         if(get_otp==otp1):
#             print("True")
#             return render(request,"profile.ntml")
#         else:
#             print("false")
#             return render(request,"otp.html")




def loginajax(request):
    return render(request, "loginajax.html")

def forget_pass(request):
    return render(request,'forget_pass.html')

@csrf_exempt
def new2(request):
    if request.method=='POST':
        data1 = Sign.objects.all()
    get_email=request.POST.get("email")
    get_contact = request.POST.get("contact_no")

    reset_pass1=Sign.objects.get(email=get_email)
    # emailid=Sign.objects.get(email=get_email)
    # reset_pass=Sign.objects.all()

    reset_pass=reset_pass1.password
    emailid=reset_pass1.email

    send_mail('Password email', str(reset_pass), 'shivam.mittal38@gmail.com', [emailid])

    return JsonResponse({"success": True,})


@csrf_exempt
def validate(request):
    dict={}
    if request.method=="GET":
        print("hello")
        email = request.GET.get('email')
        get_pwd = request.GET.get('pwd')
        data = Sign.objects.get(email=email)
        email=data.email
        pwd=data.password
        if(get_pwd==pwd):
            request.session['email'] = email
        else:
            print("invalid")
    return JsonResponse({"email": email, "success": True,})


def profile(request):
    return render(request,'index.html')

@csrf_exempt
def otp_validate(request):
    if request.method == "POST":
            otp1 = request.POST.get("otp")
            get_email=request.POST.get("email")
            print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
            # data1=Otp_match.objects.get(otp=otp1)
            # data1=Sign.objects.filter(email=get_email)
            # data1 = Otp_match.objects.select_related().filter(email=get_email)
            # data1=Sign.filter(email=Otp_match.objects.filter(email=get_email))
            # data2 = Sign.objects.filter(email=get_email).values_list('email', flat=True)
            # data1= Otp_match.objects.filter(otp=data2)
            # get = Sign.objects.get(email=get_email)
            # data1 = get.Otp_match.objects.all()

            # data1 = Sign.objects.get(email=get_email)
            # data2= Otp_match.objects.get(otp=otp1)

            # user = User.objects.get(id=1)
            # author = Author.objects.get(user)
            #
            data1 = Sign.objects.get(email=get_email)
            data2=Otp_match.objects.get(otp=otp1, user=data1)
    return JsonResponse({"success":True,})





                # data2=Otp_match.objects.get(data1)
            # print(data2)
            # data3=data2.user.email
            # print(data3)
            # # data2 = Otp_match.objects.get(email=p,otp=otp1)

            # print(data2)
            # get_otp=data2.otp
            # print(get_otp)


            # if(get_otp==otp1):
            #     print("True")
            # else:
            #     print("false")
    # if request.method=="POST":
        # print('aaaaaaaaaaaaa')

        # get_otp=request.POST.get('otp')
        # email=request.POST.get('email')
        # if(get_otp==str(otp)):
        #     print("true")
        #
        # else:
        #     print("fa


