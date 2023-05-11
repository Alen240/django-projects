from django.shortcuts import render
from django .contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def signup1(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'signup1.html',{"form":form})    
def login1(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(username=name,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse("Invalid !! NO User Found")
    return render(request,'login1.html')
def logout1(request):
    logout(request)
    return login1(request)