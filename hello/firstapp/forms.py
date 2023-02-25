from django import forms


class UserForm(forms.Form):
   time = forms.TimeField(label="Введите время")