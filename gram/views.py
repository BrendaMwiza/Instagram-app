# from django.http import HttpResponse,httpResponseRedirect
from django.shortcuts import render,redirect
from .models import Image,Profile,Comments,Follower
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import Form,NewImageForm,UpdateProForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    # date = dt.date.today()
    image_pic = Image.objects.all()

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
    return render(request, 'index.html', {"NewImageForm":form,"image_pic":image_pic})

@login_required(login_url='/accounts/login/')
def new_pic(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user_name = current_user
            picture.save()
        return redirect('addPic')

    else:
        form = NewImageForm()
    return render(request, 'everything/add-pic.html', {"form": form})

@login_required(login_url='/accounts/login/')
def getProfile(request,users=None):
    if not users:
        user = request.user
        pics = Image.objects.filter(name=users)
        return render(request,'everything/profile.html',locals())


@login_required(login_url='/accounts/login/')
def editProfile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProForm(request.POST,request.FILES)
        if form.is_valid():
            pics = form.save(commit=False)
            pics.user_name = current_user
            pics.save()
        return redirect('editProfile')

    else:
        form = UpdateProForm()
    return render(request,'everything/pro_edit.html',{"test":form})

# def users(request):
#     used = User.objects.all()
#     accounts = {'used':used}
#     return render(request,'users.html',accounts)
