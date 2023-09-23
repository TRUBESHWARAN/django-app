from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from time import ctime
from app1.forms import *
from app1.models import Enquiry, Students
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# 2 Views --> 1. Function Based views   2. Classy Views

def homePage(request):
    return render(request,'home.html')

def aboutPage(request):
    x = ctime()
    return render(request,'about.html',{'now':x,'student1':'livewire','student2':'VivEk sriNivasaN','place':'cheNNai'})

def coursePage(request):
    courses = ['Java','Python','C','C++','FUll Stack','Web Designing']
    return render(request,'course.html',{'cor':courses})

def enquiryPage(request):
    fm = EnquiryForm(request.POST or None)
    if fm.is_valid():
        fm.save()
        return HttpResponse("Form Submitted!")
    return render(request,'enquiry.html',{'form':fm})


@login_required(login_url='/login')
def enquiries(request):
    data = Enquiry.objects.all()
    return render(request,'enqs.html',{'data':data})

@login_required(login_url='/login')
def editPage(request,id):
    obj = get_object_or_404(Enquiry,pk=id)
    form = EditForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponse("Updated Successfully!")
    return render(request,'update.html',{'myform':form})

@login_required(login_url='/login')
def deletePage(request,id):
    obj = get_object_or_404(Enquiry, pk=id)
    #obj.delete()
    #return redirect('/enquiries')
    if request.method == 'POST':
        obj.delete()
        #return HttpResponse("Deleted Successfully")
        return redirect('/enquiries')
    return render(request,'delete.html',{'data':obj})

class AddStudent(CreateView):
    model = Students
    fields = "__all__"
    template_name = 'addStudent.html'
    success_url = '/'

class ViewStudents(ListView):
    model = Students
    template_name = 'viewstudents.html'
    context_object_name = 'data'
    queryset = Students.objects.all()

class UpdateStudent(UpdateView):
    model = Students
    fields = ('name','email','phone','course_name','course_fee','address')
    success_url = '/viewstudents'
    template_name = 'updatestudent.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Students,student_id=self.kwargs['id'])
        return obj

class DeleteStudent(DeleteView):
    model = Students
    template_name = 'deletestudent.html'
    success_url = '/viewstudents'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Students,student_id=self.kwargs['id'])
        return obj

@login_required(login_url='/login')
def profilePage(request):
    return render(request,'staffpage.html')

# User -> Table name
# UserCreationForm -> SignupForm

def signup(request):
    frm = SignupForm(request.POST or None)
    if frm.is_valid():
        frm.save()
        return HttpResponse("ACCOUNT CREATED SUCCESSFULLY")
    return render(request,'signup.html',{'form':frm})