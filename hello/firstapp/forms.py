from django import forms


class UserForm(forms.Form):
    city = forms.TypedMultipleChoiceField(choices=((1, "Москва"),
                                                   (2, "Воронеж"),
                                                   (3, "Курск"),
                                                   (4, "Томск")),
                                          label="Выбирите город",
                                          empty_value=None)
