from django import forms


class UserForm(forms.Form):
    country = forms.MultipleChoiceField(choices=((1, "Москва"),
                                                 (2, "Воронеж"),
                                                 (3, "Курск"),
                                                 (4, "Россия")),
                                        label="Выбирите страны")
