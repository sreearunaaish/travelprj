from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from travelapp.models import place, team


def index(request):
     places_var = place.objects.all()
     team_var = team.objects.all()
     return render(request, 'index.html',{'result_place':places_var,'result_team':team_var})
    #return render(request,'arithmetic.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        psw=request.POST['psw']
        user=auth.authenticate(username=username,password=psw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
     if request.method=='POST':
         username=request.POST['username']
         email = request.POST['email']
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         psw = request.POST['psw']
         cpsw = request.POST['psw-repeat']
         if psw==cpsw:
              if User.objects.filter(username=username).exists():
                  messages.info(request,'username taken')
                  return redirect('register')
              elif User.objects.filter(email=email).exists():
                  messages.info(request, 'email taken')
                  return redirect('register')
              else:

                   user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=psw)

                   user.save()
                   print("user created")
                   return redirect('login')
         else:
              messages.info(request,'password not matched')
              return redirect('register')
         return redirect('/')
     return render(request,'register.html')

# def arith_metic(request):
#
#      val1 = int(request.GET.get("number1", ""))
#      val2 = int(request.GET.get("number2", ""))
#      res_add=val1+val2
#      res_sub=val1-val2
#      res_mul = val1 * val2
#      res_div = val1 /val2
#      return render(request,"arithmetic_result.html",{'result_add':res_add,'result_sub':res_sub,'result_mul':res_mul,'result_div':res_div})
#
#
#
#
#

















'''
def index(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

#def detail(request):
   # return HttpResponse('Welcome to the customer detail page')
def contact(request):
    return HttpResponse('Thank you for visiting the site')
'''