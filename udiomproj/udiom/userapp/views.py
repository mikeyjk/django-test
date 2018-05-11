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
    paginate_by = 50
    ordering = ['-id']

class PersonCreate(CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person')

class PersonUpdate(UpdateView):
    model = Person
    fields = '__all__'

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('person')

def person_created(request):
    return render(request, 'person_created.html')

def create_person(request):
    if request.method == 'POST':
        form = CreatePersonForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # person.name = data.name
            # person.email = data.email
            # person.save()
            form.save()
        return HttpResponseRedirect('')
    else:
        form = CreatePersonForm()
    return render(request, 'create_person.html', {'form': form})

def search(request):
    person_list = Person.objects.all()
    person_filter = PersonFilter(request.GET, queryset=person_list)
    return render(request, 'person_list.html', {'filter': person_filter})
