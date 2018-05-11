from django.forms import ModelForm
from .models import Person
from django.core.exceptions import NON_FIELD_ERRORS

class CreatePersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        error_messages = {
                NON_FIELD_ERRORS: {
                    'unique_together': "%(model_name)s's %(field_label)s are not quniue.",
            }
        }
    # Can avoid defining clean_<fieldname>() - already inherently validated acceptably.
