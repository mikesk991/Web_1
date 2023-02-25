from django import forms


class UserForm(forms.Form):
   name = forms.CharField(label="Имя клиента", required=False, max_length=15,
                          min_length=3, help_text="ФИО не более 15 символов")

