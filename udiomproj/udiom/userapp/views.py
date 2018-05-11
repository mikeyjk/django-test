from django.http import HttpResponseRedirect
from djangow.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Person
from .forms import CreatePersonForm

def index(request):
    numPeople=Person.objects.all().count()

    return render(
        request,
        'index.html',
        context={'numPeople':numPeople},
    )

class PersonListView(generic.ListView):
    model = Person
    fields = '__all__'

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

# def create_person(request):
    # # person_instance=get_object_or_404(Person)

    # # If this is a POST request then process the Form data
    # if request.method == 'POST':
        # # Create a form instance and populate it with data from the request (binding):
        # form = CreatePersonForm(request.POST)

        # # Check if the form is valid:
        # if form.is_valid():
            # # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            # instance = form.save()
            # instance.save()

            # # redirect to a new URL:
            # # TODO define path, can't just have form success page be the same?
            # return HttpResponseRedirect(reverse_lazy('person-created') )

    # # If this is a GET (or any other method) create the default form.
    # else:
        # # form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
        # form = CreatePersonForm()

    # return render(request, 'create_person.html', {'form': form})
