from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Person
from .forms import CreatePersonForm
from .filters import PersonFilter

class PersonListView(generic.ListView):
    model = Person
    form_class = CreatePersonForm
    paginate_by = 10
    ordering = ['-id']

class PersonCreate(CreateView):
    model = Person
    form_class = CreatePersonForm
    success_url = reverse_lazy('person')

class PersonUpdate(UpdateView):
    model = Person
    form_class = CreatePersonForm

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('person')

def search(request):
    person_list = Person.objects.all()
    person_filter = PersonFilter(request.GET, queryset=person_list)
    return render(request, 'person_list.html', {'filter': person_filter})
