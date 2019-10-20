# from django.http import HttpResponse,httpResponseRedirect
from django.shortcuts import render,redirect
from .models import Image,Profile,Comments,Follower
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import Form
# Create your views here.

def index(request):
    # date = dt.date.today()
    image = Image.objects.all()

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = Recipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('index')
    else:
        form = Form()
    return render(request, 'index.html', {"picForm":form})

