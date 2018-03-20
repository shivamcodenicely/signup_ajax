from django.shortcuts import render
from .models import Sign,Otp_match,Electonics,Mobiles,Mobile_Brand,Laptops,Mobile_Model,Laptop_Brand,Laptop_Model
from django.http import HttpResponse,response
from django.http import JsonResponse
import random
from django.core.mail import send_mail
from django.shortcuts import render_to_response
import json
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.db import IntegrityError
from django.core.files.uploadedfile import SimpleUploadedFile
import os

def p(request):
    return render(request,'index.html')

def z(request):
    return render(request,'new.html')


def n(request):
    contxt={}
    if request.method=='GET':
        email=request.GET.get('Email')
    form=Sign.objects.get(email=email)
    email=form.email
    fname=form.fname
    lname=form.lname
    contact=form.contact
    contxt['email'] = email
    contxt['fname'] = fname
    contxt['lname'] = lname
    contxt['contact'] = contact

    product=Electonics.objects.all()
    # print(product)

    mobile_list=[]
    for i in product:
        product_dict = {'id':i.id,'name':i.product_name}
        mobile_list.append(product_dict)

    product1 = Mobiles.objects.all()
    mobile_list1 = []

    for j in product1:
        prod = Mobiles.objects.get(id=j.id)

        mobile_dict= {'id':j.id,'name':j.brand_name, 'pid':prod.mobile_user.id}
        mobile_list1.append(mobile_dict)
    # print(mobile_list1)

    product3=Mobile_Brand.objects.all()
    mobile_list2 = []
    for k in product3:

        prod = Mobile_Brand.objects.get(id=k.id)
        mobile_dict3 = {'id': k.id,'name': k.model_name,'pid':prod.mobile_brand_user.id}
        mobile_list2.append(mobile_dict3)
    # print(mobile_list2)

    laptop_list=[]
    product4=Laptops.objects.all()

    for l in product4:
        prod = Laptops.objects.get(id=l.id)
        laptop_dict={'id':l.id,'name':l.brand_name,'pl_id':prod.laptop_user.id}
        laptop_list.append(laptop_dict)
    # print(laptop_list)

    product5=Laptop_Brand.objects.all()
    laptop_list1=[]
    for m in product5:
        prod = Laptop_Brand.objects.get(id=l.id)
        laptop_dict1={'id':m.id, 'name':m.brand_name,'pl_id':prod.laptop_brand_user.id }
        laptop_list1.append(laptop_dict1)

    product6=Laptop_Model.objects.all()
    laptop_list2=[]
    for n in product6:
        laptop_dict2={'id':n.id,'name':n.model_name}
        laptop_list2.append(laptop_dict2)
    return render(request,'profile.html',{'contxt':contxt,
                                          'mobile_dict':mobile_dict,
                                          'mobile_dict3':mobile_dict3,
                                          'mobile_list1':mobile_list1,
                                          'mobile_list':mobile_list,
                                          'mobile_list2':mobile_list2,
                                          'laptop_list':laptop_list,
                                          'laptop_list1':laptop_list1,
                                          'laptop_list2':laptop_list2})



@csrf_exempt
def jprod1(requset):
    try:

        product = Electonics.objects.all()
        mobile_list = []
        for i in product:
            product_dict = {'id': i.id, 'name': i.product_name}
            mobile_list.append(product_dict)
    except Exception as e:
        print(e)
    return JsonResponse({"success": True,'mobile_list':mobile_list})



def profile1(request):
    if request.method=="GET":
        mobile_list=request.GET.get('mobile_list')

        return render(request,'profile1.html',{'mobile_list':mobile_list})



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
        # print("hello")
        profile_picture=request.FILES('profile_picture')
        # print("not")
        # folder='media/'
        # full_path=os.path.join(folder,profile_picture)
        #
        # f=open(folder+profile_picture+'w')
        # file_content=request.FILES.get('profile_picture').read()
        # f.write(file_content)
        # f.close()
        #
        # print("@W@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # print(f)
        #
        #
        # image = request.FILES.get('file').name
        # folder = 'media' + '/signature/'
        # full_filename = os.path.join(folder, image)
        #
        # fout = open(folder + image, 'w')
        #
        # file_content = request.FILES.get('file').read()
        #
        # fout.write(file_content)
        #
        # fout.close()





        try:
            emp = Sign.objects.create(fname=fname, lname=lname, username=uname, password=pwd, email=email,
                                    contact=contact,profile_picture=profile_picture)

            emp.save()
        except IntegrityError:
            return JsonResponse({"success": False,})
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


        # request.session['email']=email

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
    # get_contact = request.POST.get("contact_no")

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
    if request.method=="POST":
        email = request.POST.get('email')
        get_pwd = request.POST.get('pwd')
        data = Sign.objects.get(email=email)
        email=data.email
        pwd=data.password
        print(pwd)
        print(get_pwd)
        if(get_pwd==pwd):
            request.session['email'] = email
            return JsonResponse({"email": email, "success": True})
        else:
            print("ppppppppp")
            return JsonResponse({"success": False})

    # return JsonResponse({"email": email, "success": True})


def profile(request):
    return render(request,'index.html')

@csrf_exempt
def otp_validate(request):
    if request.method == "POST":
            otp1 = request.POST.get("otp")
            get_email=request.POST.get("email")
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


