from django.shortcuts import render
from .models import Participant 
from django.core.exceptions import ValidationError
# Create your views here.


def home(request):
    context = {}
    return render(request, 'eventapplication/home.html', context)


def register(request):
    context = {}
    if request.method == 'POST':
        p1 = Participant()
        p1.name = request.POST.get('name', '-')
        p1.email = request.POST.get('email', '-')
        p1.Phonenumber = request.POST.get('Phonenumber', '000')
        p1.interest = request.POST.get('interest', '-')
        p1.institutionname = request.POST.get('institutionname', '-')

        if len(Participant.objects.all()) > 15:
            return render(request, 'eventapplication/failed.html', context)

        else:
            p1.save()
            return render(request, 'eventapplication/success.html', context)

    if request.method == 'GET':
          context['name'] = ''
          context['email'] = ''
          context['phonenumber'] = ''
          context['interest'] = ''
          context['institutionname'] = ''

    return render(request, 'eventapplication/register.html', context)



def success(request):
    context = {}
    return render(request, 'eventapplication/success.html', context)


def failed(request):
    context = {}
    return render(request, 'eventapplication/failed.html', context)


def listofparticipants(request):
    context = {}

    context['participants'] = Participant.objects.all()
    
    return render(request, 'eventapplication/listofparticipants.html', context)
