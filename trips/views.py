from django.shortcuts import render, redirect
from .models import Destinations,Feedback
from .forms import FeedbackForm
# from django.contrib.auth.models import Feedback

def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        form.save()
        return redirect('home')
    else:
        form = FeedbackForm()
    dests = Destinations.objects.all()
    return render(request,'index.html', {'dests': dests, 'form': form})

def feedback(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Content = request.POST['Content']
        
        feedback = Feedback.objects.create(Name = Name, Email = Email, Content = Content)
        feedback.save()
        print('form submit')
        return redirect('home')

    else:
        return render(request, 'index.html')