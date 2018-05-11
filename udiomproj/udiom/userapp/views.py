from django.shortcuts import render
from .models import Person

def index(request):
    numPeople=Person.objects.all().count()

    return render(
        request,
        'index.html',
        context={'numPeople':numPeople},
    )
