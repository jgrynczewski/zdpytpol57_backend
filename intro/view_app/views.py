from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse
from django import views

# Widoki generyczne
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import CreateView

from view_app.models import Person
from view_app.forms import PersonForm


# function-based view (widok funkcyjny)
def hello(request):
    return HttpResponse("Hello, world!")


# class-based view (widok klasowy)
class Hello(views.View):
    def get(self, request):
        return HttpResponse("Hello, world!")

# WYŚWIETLANIE SZABLONU

# function-based view
def template_hello(request):
    return render(
        request,
        'view_app/hello.html'
    )


# class-based view
class HelloView(views.View):
    def get(self, request):
        return render(
            request,
            'view_app/hello.html'
        )


# generic view (widok generyczny)
class HelloGenericView(TemplateView):
    template_name = 'view_app/hello.html'


# PRZEKAZYWANIE ZMIENNEJ DO SZABLONU

# widok funkcyjny
def template_hello2(request):
    name = "Adam"

    return render(
        request,
        'view_app/hello2.html',
        context={
            'name': name
        }
    )


# widok klasowy
class HelloClassView2(views.View):
    def get(self, request):
        name = "Adam"

        return render(
            request,
            'view_app/hello2.html',
            context={
                'name': name
            }
        )


# widok generyczny
class HelloGenericView2(TemplateView):
    template_name = 'view_app/hello2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Adam'
        return context


# DETAIL VIEW (WIDOK SZCZEGÓŁU)

# widok funkcyjny
def person_detail(request, id):
    person = get_object_or_404(Person, id=id)

    return render(
        request,
        'view_app/person_detail.html',
        context={
            'person': person
        }
    )


# Widok klasowy
class PersonView(views.View):
    def get(self, request, id):
        person = get_object_or_404(Person, id=id)

        return render(
            request,
            'view_app/person_detail.html',
            context={
                'person': person
            }
        )


# widok generyczny
class PersonDetailView(DetailView):
    model = Person

# C (CRUD)


# widok funkcyjny
def create_person(request):
    if request.method == "GET":
        form = PersonForm()

        return render(
            request,
            'view_app/create_person.html',
            context={
                'form': form,
            }
        )
    elif request.method == "POST":
        form = PersonForm(request.POST)
        form.save()

        return redirect('view_app:create_person')


# widok klasowy
class PersonCreateView(views.View):
    def get(self, request):
        form = PersonForm()

        return render(
            request,
            'view_app/create_person.html',
            context={
                'form': form,
            }
        )

    def post(self, request):
        form = PersonForm(request.POST)
        form.save()

        return redirect('view_app:create_person')


# widok generyczny
class PersonGenericCreateView(CreateView):
    model = Person
    fields = "__all__"
