from django.shortcuts import render,redirect
from django.http import HttpResponse,httpResponseRedirect
from .models import Image,Profile,Comments,Follower
from .email import send_welcome_email


# Create your views here.

def index(request):
    return render(request,'index.html')

 