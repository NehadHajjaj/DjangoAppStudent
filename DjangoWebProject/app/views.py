"""
Definition of views.
"""

from datetime import datetime
from django.http import HttpRequest
from .models import student, teacher
from .forms import studentForm, teacherForm
from django.shortcuts import (get_object_or_404, 
                              render, 
                              HttpResponseRedirect)

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def recommendationPage(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/recommandation.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def studentProfile(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    # Retrieve all contacts in the database table
    student_list = student.objects.order_by('studant_name') 
  
    return render(
        request,
        'app/profile(student,company).html',
        {
            'title':'Student',
            'message':'Your student page.',
            'year':datetime.now().year,
            'contact_list': student_list, # Embed data into the HttpResponse object
        }
    )

def teacherProfile(request):
    assert isinstance(request, HttpRequest)

    # Retrieve all contacts in the database table
    teacher_list = teacher.objects.order_by('teach_name') 
  
    return render(
        request,
        'app/profile(teacher).html',
        {
            'title':'Teacher',
            'message':'Your teacher page.',
            'year':datetime.now().year,
            'contact_list': teacher_list, # Embed data into the HttpResponse object
        }
    )

# update view for details 
def editStudent(request, id):
    # fetch the object related to passed id 
    obj = student.objects.get(stu_id = int(id))
    # pass the object as instance in form 
    form = studentForm(request.POST or None, instance = obj)
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save()
    
    student_list = student.objects.order_by('studant_name') 
    return render(
        request,
        'app/profile(student,company).html',
        {
            'title':'Student',
            'message':'Your student page.',
            'year':datetime.now().year,
            'contact_list': student_list, # Embed data into the HttpResponse object
        }
       )

# update view for details 
def editTeacher(request, id):
    # fetch the object related to passed id 
    obj = teacher.objects.get(teach_id = int(id))
    # pass the object as instance in form 
    form = teacherForm(request.POST or None, instance = obj)
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save()
    
    teacher_list = teacher.objects.order_by('teach_name') 
    return render(
        request,
        'app/profile(teacher).html',
        {
            'title':'Teacher',
            'message':'Your teacher page.',
            'year':datetime.now().year,
            'contact_list': teacher_list, # Embed data into the HttpResponse object
        }
       )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
