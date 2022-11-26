from django.shortcuts import render, redirect

from form_app5.models import Message
from form_app5.forms import ContactForm
from form_app5.forms import MessageForm


# Formularz html
def contact1(request):
    if request.method == "POST":
        data = request.POST

        Message.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            category=data.get('category'),
            subject=data.get('subject'),
            body=data.get('body'),
            date=data.get('date'),
            time=data.get('time'),
        )

        return redirect('form_app5:contact1')

    return render(
        request,
        'form_app5/contact1.html'
    )


# Formularz Django
def contact2(request):
    if request.method == "POST":
        form = ContactForm(request.POST)  # bound form - formularz związany

        if form.is_valid():
            data = form.cleaned_data

            Message.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                category=data.get('category'),
                subject=data.get('subject'),
                body=data.get('body'),
                date=data.get('date'),
                time=data.get('time')
            )

        return redirect('form_app5:contact2')

    form = ContactForm()  # unbound form - formularz niezwiązany
    return render(
        request,
        'form_app5/contact2.html',
        context={
            'form': form,
        }
    )


# Formularz modelu Django
def contact3(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        form.save()

        return redirect('form_app5:contact3')

    form = MessageForm()
    return render(
        request,
        'form_app5/contact3.html',
        context={
            'form': form,
        }
    )
