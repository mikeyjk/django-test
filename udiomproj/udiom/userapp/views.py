from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Person
from .forms import CreatePersonForm

def index(request):
    # numPeople=Person.objects.all().count()

    return render(
        request,
        'index.html',
        # context={'numPeople':numPeople},
    )

class PersonListView(generic.ListView):
    model = Person
    paginate_by = 50
    ordering = ['-id']

class PersonCreate(CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('people')

class PersonUpdate(UpdateView):
    model = Person
    fields = '__all__'

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('people')

def person_created(request):
    return render(request, 'person_created.html')

def create_person(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = CreatePersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.name = request.name
            person.email = request.email
            person.save()
            return HttpResponseRedirect(reverse_lazy('person-created') )
    else:
        form = CreatePersonForm()
    return render(request, 'create_person.html', {'form': form})
