from django import forms


class UserForm(forms.Form):
   file_path = forms.FilePathField(label="Выбирите файл",
                                   path="c:/Windows/",
                                   allow_files=True,
                                   allow_folders=True)