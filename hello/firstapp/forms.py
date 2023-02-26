from django import forms


class UserForm(forms.Form):
    ling = forms.ChoiceField(choices=((1, "Английский"),
                                      (2, "Немецкий"),
                                      (3, "Французский")), label="Выбирите язык")
