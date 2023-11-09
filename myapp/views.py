from django.shortcuts import render
from myapp.forms import EmployeeForm
from myapp.models import Employee

# Create your views here.
def home(request):
    return render(request, 'index.html')

def mygallary(request):
    return render(request,  'gallery.html')

def aboutus(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contact.html')

def join(request):
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'join.html')
    else:
        return render(request,'join.html')

def details(request):
    members = Employee.objects.all()
    return render(request, 'details.html',{'all':members})


