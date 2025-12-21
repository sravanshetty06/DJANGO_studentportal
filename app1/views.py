from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from app1.models import Student

# --- Home Page ---
def home(request):
    return render(request, "app1/home.html")

# --- Create (Add Student) ---
def addstudenttemp(request):
    return render(request, "app1/addstudent.html")

def addstudent(request):
    try:
        name = request.GET['name']
        age = request.GET['age']
        email = request.GET['email']
        dob = request.GET['dob']
        cell = request.GET['cell']
        
        std = Student(name=name, age=age, email=email, dob=dob, cell=cell)
        std.save()
        
        return render(request, "app1/success.html", {'name': name})
    except Exception as e:
        return HttpResponse(f"Error adding student: {e}")

# --- Read (Dashboard & Search) ---
def manage_students(request):
    query = request.GET.get('q', '')
    
    if query:
        # Smart search: Name OR Email
        students = Student.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query)
        )
    else:
        students = Student.objects.all().order_by('-id') # Newest first

    # Stats for Dashboard
    total_students = Student.objects.count()
    
    context = {
        'students': students,
        'query': query,
        'total_count': total_students
    }
    return render(request, "app1/manage_students.html", context)


# --- Update (Edit Student) ---
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        # Simple POST handling without Django Forms class (keeping it vanilla as per current setup)
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.dob = request.POST.get('dob')
        student.cell = request.POST.get('cell')
        student.save()
        return redirect('manage_students')

    return render(request, "app1/update_student.html", {'student': student})


# --- Delete ---
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        student.delete()
        return redirect('manage_students')
        
    return render(request, "app1/delete_confirm.html", {'student': student})


# --- Legacy Redirects (Optional, keeping for compatibility) ---
def displaytemp(request):
    return redirect('manage_students')

def display(request):
    return redirect('manage_students')