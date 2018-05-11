from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('people', views.Person.as_view(), name='person'),
    path('person/create/', views.PersonCreate.as_view(), name='person_create'),
    path('person/<int:pk>/update/', views.PersonUpdate.as_view(), name='person_update'),
    path('person/<int:pk>/delete/', views.PersonDelete.as_view(), name='person_delete'),
]
