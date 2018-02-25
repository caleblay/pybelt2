from __future__ import unicode_literals
from .models import User, Appointment
from django.shortcuts import render, redirect
from django.contrib import messages
from time import gmtime, strftime
from datetime import datetime

def index(request):
    return render(request, 'login/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/success')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    app = Appointment.objects.all().order_by('-time')
    z =[]
    for x in app:
        if x.date == datetime.now().date():
            z.append(x)
    w =[]
    print request.session['user_id']

    for x in app:
        if request.session['user_id'] == x.fkonetom.id:
            w.append(x)
    print w

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'apps': Appointment.objects.order_by('date'),
        'v':z,
        'q':w
    }
    return render(request, 'login/success.html', context)

def new(request):
    user = User.objects.get(id=request.session['user_id'])
    errors = Appointment.objects.validate_appointment(request.POST)
    if len(errors) == 0:


        user = User.objects.get(id=request.session['user_id'])
        appointment = Appointment.objects.create(task=request.POST['task'],status=request.POST['status'], date=request.POST['date'], time=request.POST['time'], fkonetom=user)

    else: 
        for err in errors:
            messages.error(request, err)
        return redirect('/success')

    return redirect('/success')

def add_new(request):
    return render(request, 'login/new.html')

def item(request, id):
    app = Appointment.objects.get(id=id)
    context = {
        'apps': app
    }

    return render(request, 'login/item.html', context)

def edit(request, id):
    b = Appointment.objects.get(id=id)
    context = {
        'b':b
    }
    return render(request, 'login/appointment.html', context)

def update(request, id):
    errors = Appointment.objects.validate_appointment(request.POST)
    b = Appointment.objects.get(id=id)
    if len(errors) == 0:
        b.task=request.POST['task']
        b.status=request.POST['status'] 
        b.date=request.POST['date'] 
        b.time=request.POST['time']
        b.save()
    else: 
        for err in errors:
            messages.error(request, err)
        return render(request, 'login/appointment.html')


    return redirect('/success')

def delete(request, id):
    b = Appointment.objects.get(id=id)
    b.delete()
    return redirect('/success')

 
