from django import forms

from form_app5.models import Message


# formularz Django
class ContactForm(forms.Form):

    CHOICES = [
        (0, "Pytanie"),
        (1, "Inne")
    ]

    name = forms.CharField(label="Imię")
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(
        choices=CHOICES,
        label="Kategoria"
    )
    subject = forms.CharField(label="Temat")
    body = forms.CharField(
        label="Treść",
        widget=forms.Textarea(
            attrs={"cols": 40, "rows": 10}
        )
    )
    date = forms.DateField(
        label="Ulubiona data",
        widget=forms.widgets.NumberInput(
            attrs={"type": "date"}
        )
    )
    time = forms.TimeField(
        label="Ulubiona godzina",
        widget=forms.widgets.NumberInput(
            attrs={"type": "time"}
        )
    )


# formularz modelu
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # fields = [
        #     'name',
        #     'email',
        #     'category',
        #     'subject',
        #     'body',
        #     'date',
        #     'time'
        # ]
        # exclude = ['body']
        fields = "__all__"
        labels = {
            "name": "Imię",
            "email": "Email",
            "category": "Kategoria",
            "subject": "Temat",
            "body": "Treść",
            "date": "Ulubiona data",
            "time": "Ulubiona godzina",
        }
        widgets = {
            "date": forms.widgets.NumberInput(
                attrs={'type': 'date'}
            ),
            "time": forms.widgets.NumberInput(
                attrs={'type': 'time'}
            )
        }
