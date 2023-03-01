from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from.models import User,Department,Employees
from datetime import datetime
from django.utils import timezone


# Create your views here.

###########  admin ################
def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect(admin_home)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(admin_home)
        else:
            return redirect('/')
    return render(request,'adminLogin.html')

def admin_home(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method=='POST':
            name = request.POST['DptName']
            description = request.POST['description']
            filename = request.FILES.get('image')
            fdate = request.POST.get('date')
            print(filename)
            print(fdate)
            depmt = Department(DptName = name,image = filename,description = description,yearFounded = fdate)
            depmt.save()
        department = Department.objects.all()
        context = {'department':department}
        return render(request,'adminHome.html',context)
    else:
        return redirect(admin_login)

def logoutadmin(request):
    if request.user.is_authenticated and request.user.is_staff:
        logout(request)
    return redirect(admin_login)

def addHeadUser(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method=='POST':
            name = request.POST['name']
            age = request.POST['age']
            description = request.POST['description']
            filename = request.FILES.get('image')
            department = request.POST['department']
            print(int(department))
            d = Department.objects.get(id = department)
            print(d.id)
            ins = Employees(name = name,age = age,profile = filename,department = Department.objects.get(id = int(department)))
            ins.save()
            return redirect(addHeadUser)
        dep = Department.objects.all()
        user =Employees.objects.all()
        print(user)
        context = {'user':user,'dep':dep}
        return render(request,'headuser.html',context)

def deleteHeaduser(request,id):
    print(id,'kkkkkkkkkkkkkkkkkkkkkk')
    emp = Employees.objects.filter(id = id)
    emp.delete()
    print(emp)
    return redirect(addHeadUser)

def editHeaduser(request,id):
    pass








