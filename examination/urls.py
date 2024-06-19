from django.urls import path

from . import views

app_name = "examination"


urlpatterns = [
    path("persons/", views.get_persons, name="persons"),
    path("persons/<int:pk>", views.get_person, name="person"),
    path("persons/<int:pk>/delete", views.delete_person, name="person_delete"),
]