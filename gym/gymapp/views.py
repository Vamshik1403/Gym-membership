from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Product,Cart
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from gymapp.models import Enrollment,Attendance,MembershipPlan,Trainer
# import razorpay
# Create your views here.



def home(request):
    context={}
    products=Product.objects.filter(is_active=True)
    context['products']=products
    return render(request,"index.html",context)

def user_login(request):
     context={}
     if(request.method=="POST"):
          uname=request.POST['uname']
          upass=request.POST['upass']
          if uname=='' or upass=='':
               context['error']="Please fill all the fields"
               return render(request,"login.html",context)
          else:
               u=authenticate(username=uname,password=upass)
               if u is not None:
                   login(request,u)
                   return redirect("/home")
               else:
                   context['error'] = "Invalid credentials"
                   return render(request,"login.html",context)
          
     else:
          return render(request,"login.html")


def user_register(request):
    context={}
    if(request.method == 'POST'):
        fname = request.POST['fname']
        uname = request.POST['uname']
        email=request.POST['email']
        phno=request.POST['phno']
        upass = request.POST['upass']
        ucpass = request.POST['ucpass']
        if fname == '' or uname == '' or upass == '' or ucpass == '' or email == '' or phno == '':
            context['error']="Please fill all the fields"
            return render(request,"registration.html",context)
        elif upass!=ucpass:
            context['error']="Password and Confirm password must be same"
            return render(request,"registration.html",context)
        else:
            user_obj = User.objects.create(password=upass,username=uname,email=email)
            user_obj.set_password(upass)
            user_obj.save()
            context['success']="User registered successfully"
            return render(request,"registration.html",context)
    else:
        return render(request,"registration.html")
     


def user_logout(request):
    logout(request)
    return redirect("/home")

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    attendance=Attendance.objects.filter(phonenumber=user_phone)
    print(posts)
    context={"posts":posts,"attendance":attendance}
    return render(request,"profile.html",context)

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        phonenumber=request.POST.get('PhoneNumber')
        Login=request.POST.get('logintime')
        Logout=request.POST.get('loginout')
        SelectWorkout=request.POST.get('workout')
        TrainedBy=request.POST.get('trainer')
        query=Attendance(phonenumber=phonenumber,Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,TrainedBy=TrainedBy)
        query.save()
        messages.warning(request,"Attendace Applied Success")
        return redirect('/attendance')
    return render(request,"attendance.html",context)

def enrollment(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return render(request,"enroll.html")

    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('/join')
    return render(request,"enroll.html",context)


def bmi(request):
    return render(request,"bmi.html")

def fo(request):
    return render(request,"footer.html")

def hd(request):
     return render(request,"header.html")

def price(request):
     return render(request,"pricing.html")

def product(request):
    context={}
    products=Product.objects.filter(is_active=True)
    context['products']=products
    return render(request,"product.html",context)

def prog(request):
     return render(request,"program.html")

def productdetails(request,pid):
    context={}
    product = Product.objects.get(id=pid)
    context['product']=product
    return render(request,"productdetails.html",context)


def pay(request):
    client = razorpay.Client(auth=("rzp_test_Gp87o4Re7G6P6a", "fdMXOofHxYiPDAei5qXeIiEi"))
    data = { "amount": 5000*2, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    print(payment)
    context={}
    context['payment']=payment
    return render(request,"pay.html",context)

def addToCart(request,pid):
    if request.user.is_authenticated:
        uid=request.user.id
        u=User.objects.get(id=uid)
        p=Product.objects.get(id=pid)
        c=Cart.objects.create(uid=u,pid=p)
        c.save()
        return redirect("/addtocart")
    else:
        return redirect("/login")




# def senduseremail(request):
#     msg="Order placed successfully"
#     send_mail(
#     "Cart Order",
#     msg,
#     "Here is the message.",
#     "imvam12@gmail.com",
#     ["imvam12@gmail.com"],
#     fail_silently=False,
#     )
#     return redirect("/")
    


    # response = requests.get('https://www.imdb.com/title/tt1439629/episodes?season=' + str(sn))