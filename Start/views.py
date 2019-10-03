from .models import data
from django.contrib import messages,auth
from django.shortcuts import render,redirect
from rest_framework import  viewsets
from .serializers import dataSerializer
from rest_framework.authentication import TokenAuthentication

class dataViewSet(viewsets.ModelViewSet):
    serializer_class =  dataSerializer
    queryset = data.objects.all()
    authentication_classes = {TokenAuthentication}
def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')

def query(request):
    if request.method=='POST':
      Name=request.POST['Name']
      Email=request.POST['Email']
      Course=request.POST['Course']
      Sem=request.POST['Sem']
      Subjects=request.POST['Subjects']
      Query=request.POST['Query']
      user =data.objects.create(Name=Name,Email=Email,Course=Course,Sem=Sem,Subjects=Subjects,Query=Query)
      user.save();
      messages.success(request,"Query Raised")
      return redirect(query)
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You Are Logged In')
            return redirect(dashboard)
        else:
            messages.error(request,'Invalid Credentials')
            return redirect(login)
    else:
        return render(request,'login.html')

def dashboard(request):
    info=data.objects.all()
    que = {
        'query':data
    }
    return render(request,'dashboard.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You Are Logged Out')
        return redirect(index)