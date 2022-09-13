from http.client import HTTPResponse
from select import select
from django.shortcuts import render
from django.http import HttpResponse
from .models import meetup

# Create your views here.


def meetups_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetups',
        'description': 'this is the first meetup!'
    }
    return render(request, 'meetups/all-meetups.html',
                  {
                      'meetup_title': selected_meetup['title'],
                      'meetup_description': selected_meetup['description']
                  })


def index(request):
    meetups = meetup.objects.all()
    return render(request, 'meetups/index.html', {'meetups': meetups})
