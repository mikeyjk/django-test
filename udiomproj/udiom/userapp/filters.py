from .models import Person
import django_filters

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = '__all__'
