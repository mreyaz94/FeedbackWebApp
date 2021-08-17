from django import forms
from django.core import validators


# def start_with_d(value):
#      if value[0].lower() != 'd':
#         raise forms.ValidationError('Name must be start with D')
# def only_gmail(value):
#     if value[-10:] != '@gmail.com':
#         raise forms.ValidationError('Only must be gmail')

# def start_is_alpha(value):
#     if value.isalpha() != True:
#         raise forms.ValidationError('Name must be only alphabets')

class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean(self):
        # print('Total Form Valiadtion...')
        cleaned_data = super().clean()
        inputname = cleaned_data['name']
        if len(inputname) < 10:
            raise forms.ValidationError('Name must be conatins minimum 10 character')
        inputrollno = cleaned_data['rollno']
        if len(str(inputrollno)) != 3:
            raise forms.ValidationError('Rollno must be contain 3 digits')
