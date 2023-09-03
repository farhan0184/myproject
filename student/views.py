from django.shortcuts import render, redirect

# Create your views here.
from django.core import serializers
from student.models import PersonInfoCreate,Results,Subjects

from django.contrib.auth import authenticate, login
from django.contrib import messages



def home(request):
    person = PersonInfoCreate.objects.filter(userid='CSE110001').values()
    
    if request.method == "POST":
        userid = request.POST.get('userid')
        password =request.POST.get('password')
        if PersonInfoCreate.objects.filter(userid=userid).values().exists() and password == userid:

            url = f'/dashboard/?userid={userid}'
            
            return  redirect(url)

    return render(request, 'home.html')



def dashboard(request):
    userid = request.GET.get('userid','')
    person = PersonInfoCreate.objects.filter(userid=userid).values()
    result = Results.objects.all()
    student_result = {}
    student_info = ''
    for x in person:
        student_info=x
    
    
        
    for x in range(0,len(result)):
        if result[x].subject.person.userid == userid:
            # print(result[x].result)
            student_result[result[x].subject.sub] = result[x].result

    information = {
        'name': student_info['name'],
        'email': student_info['email'],
        'userid': userid,
        'section': student_info['section'],
        'result': student_result,
    }
    return render(request, 'dashboard.html',information)