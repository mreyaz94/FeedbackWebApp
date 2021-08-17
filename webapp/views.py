from django.shortcuts import render
from . import forms

# Create your views here.


def thankyou_view(request):
    return render(request,'webapp/thankyou.html')


def feedback_view(request):
    if request.method == 'GET':
        form = forms.FeedBackForm()
    #return render(request, 'webapp/feedback.html',dict)
    if request.method == 'POST':
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation success and printing feedback info')
            print('Student Name:',form.cleaned_data['name'])
            print('Student Rollno:',form.cleaned_data['rollno'])
            print('Student Email Id:',form.cleaned_data['email'])
            print('Student Feedback:',form.cleaned_data['feedback'])
            return render(request,'webapp/thankyou.html')
    return render(request, 'webapp/feedback.html',{'form':form})