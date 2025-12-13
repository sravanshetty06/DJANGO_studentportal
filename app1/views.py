from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from app1.models import Student
# Create your views here.

def home(request):
    response=render(request,"app1/home.html")
    return response

def addstudenttemp(request):
    response=render(request,"app1/addstudent.html")
    return response


def addstudent(request):
        name=request.GET['name']
        age=request.GET['age']
        email=request.GET['email']
        dob=request.GET['dob']
        cell=request.GET['cell']
        std=Student(name=name,age=age,email=email,dob=dob,cell=cell)
        std.save()
        msg=f"student added added successfully"
        return HttpResponse(msg)
def displaytemp(request):
    response=render(request,"app1/display.html")
    return response
def display(request):
    name=request.GET['name']
    std11=Student.objects.all().filter(name=name)
    if len(std11)!=0:
        response=render(request,"app1/displaystudent.html",context={'std11':std11})
        return response
    else:
        return HttpResponse(f"student doesnot exist")
"""def display(request):
    name = request.GET.get('name')

    print("SEARCH NAME:", name)   # 🔴 DEBUG LINE

    if name:
        students = Student.objects.filter(name__icontains=name)
    else:
        students = Student.objects.all()

    print("RESULT COUNT:", students.count())  # 🔴 DEBUG

    return render(request, 'display.html', {'students': students})"""
"""def delete_student(request, id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=id)
        student.delete()
    return redirect('display')"""