import json

from django.shortcuts import get_object_or_404, render, redirect
from .models import Person
from .forms import NameForm1, PersonForm


def get_persons(request):
    persons = Person.objects.all()
    context = {"persons": persons}
    return render(request, "examination/persons.html", context)


def get_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    context = {"person": person}
    return render(request, "examination/person.html", context)


def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('examination:persons')
    else:
        form = PersonForm()
    return render(request, "examination/person_add.html", {'form': form})


def add_person_2(request):
    if request.method == "POST":
        form = NameForm1(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            person = Person(
                first_name=data['first_name'],
                last_name=data['last_name'],
                birth_day=data['birth_day'],
            )
            person.save()
        return redirect('examination:persons')
    return render(request, "examination/person_add.html")


def add_person_1(request):
    context = {"person": 1}
    if request.method == "POST":
        data = request.POST
        person = Person(
            first_name=data['your_name'],
            last_name=data['last_name'],
            birth_day=data['birth_day'],
        )
        person.save()
        return redirect('examination:persons')
    return render(request, "examination/person_add_1.html", context)


def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    context = {"person": person}
    if request.method == "POST":
        person.delete()
        return redirect('examination:persons')
    return render(request, "examination/person_delete.html", context)


