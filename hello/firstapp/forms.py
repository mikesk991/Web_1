from django import forms


class UserForm(forms.Form):
    city = forms.TypedChoiceField(choices=((1, "Москва"),
                                           (2, "Воронеж"),
                                           (3, "Курск")),
                                  label="Выбирите город",
                                  empty_value=None)
