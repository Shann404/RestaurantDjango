from contextlib import redirect_stderr
from urllib import request

from django.shortcuts import render, redirect
from Food.models import Booking
from Food.models import Info
def index(request):
    return render(request,'index.html')

def insertdata(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people= request.POST['people']
        message = request.POST['message']

        book=Booking(name=name,
                     email=email,
                     phone=phone,
                     date=date,
                     time=time,
                     people=people,
                     message=message
                     )

        book.save()
        return redirect('/viewdata/')

    return render(request,'index.html')

def get_customer(request, id):
    book = Booking.objects.get(id=id)
    return render(request,"details.html",{"book":book})

def UpdateReq(request, id):
    book = Booking.objects.get(id=id)

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']

        book.name = name
        book.email = email
        book.phone = phone
        book.date = date
        book.time = time
        book.people = people
        book.message = message

        book.save()

        return redirect('/viewdata/')
    return render(request,"update.html", {"book":book})

def deleteReq(request, id):
    book = Booking.objects.get(id=id)
    book.delete()
    return redirect('/viewdata/')


def viewdetails(request):
    bookings = Booking.objects.all()
    return render(request, 'view.html', {"bookings":bookings})

def sendInfo(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send=Info(name=name,
                  email=email,
                  subject=subject,
                  message=message)

        send.save()
        return redirect('/viewInfo/')

    return render(request,"index.html")

def viewInfo(request):
        information=Info.objects.all()
        return render(request, "SendInfo.html", {"information":information})

def getInfo(request, id):
    information=Info.objects.get(id=id)
    return render(request, "viewDetails.html", {"information":information})

def updateInfo(request, id):
    information=Info.objects.get(id=id)

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        information.name = name
        information.email = email
        information.subject = subject
        information.message = message

        information.save()
        return redirect('/viewInfo/')

    return render(request,"updateInfo.html", {"information":information})

def deleteInfo(request, id):
    information=Info.objects.get(id=id)
    information.delete()
    return redirect('/viewInfo/')


# Create your views here.
