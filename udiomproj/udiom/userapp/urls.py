from django.urls import path
from django_filters.views import FilterView
from . import views
from .filters import PersonFilter

urlpatterns = [
    path('', views.PersonListView.as_view(), name='person'),
    path('search/', FilterView.as_view(filterset_class=PersonFilter, template_name='person_filter.html'), name='search'),
    path('person/create/', views.PersonCreate.as_view(), name='person_create'),
    path('person/<int:pk>/update/', views.PersonUpdate.as_view(), name='person_update'),
    path('person/<int:pk>/delete/', views.PersonDelete.as_view(), name='person_delete'),
]
