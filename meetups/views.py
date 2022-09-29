from django.shortcuts import render
from .models import meetup

# Create your views here.


def meetups_details(request, meetup_slug):
    try:
        selected_meetup = meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/all-meetups.html',
                      {
                          'meetup_found': True,
                          'meetup_title': selected_meetup.title,
                          'meetup_description': selected_meetup.description
                      })

    except Exception as exc:
        return render(request, 'meetups/all-meetups.html', {
            'meetup_found': False,
        })


def index(request):
    meetups = meetup.objects.all()
    return render(request, 'meetups/index.html', {'meetups': meetups})
