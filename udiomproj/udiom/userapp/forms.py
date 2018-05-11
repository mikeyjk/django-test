from django.forms import ModelForm
from .models import Person
from django.core.exceptions import NON_FIELD_ERRORS

class CreatePersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
