from django import forms
from django.core.mail import EmailMessage

from .models import ShoppingList


class ListCreateForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ('product',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
