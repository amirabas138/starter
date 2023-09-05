from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from pyexpat.errors import messages

# Create your views here.
from .forms import *
from .models import MyUser
from django.contrib.auth import authenticate, login, logout


def Login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('login')
            # Redirect to a success page.
        else:
            return HttpResponse('false login')
            # Return an 'invalid login' error message.
    else:
        return render(request, 'shop/login.html')


def Register(request):
    if request.user.is_authenticated:
        return redirect('shop:home')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        username = form['username'].value()
        email = form['email'].value()
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(email=data['email'], username=data['username'], password=data['password'])
            user.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('not')
    else:
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'shop/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect("shop:login")


def home(request):
    return render(request, 'shop/home.html')


def ProfileUpdate(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.Profile)
        if profile_form.is_valid() or user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Update Successfully', 'success')
            return redirect('administrator:home')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.Profile)
    context = {'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'shop/UpdateProfile.html', context)


def index(request):
    post = Post.objects.filter(status='p').order_by('-publish')
    context = {
        'post': post
    }
    return render(request, 'shop/index.html', context)


def singlePost(request, slug):
    post = get_object_or_404(Post, slug=slug, status='p')
    context = {
        'post': post
    }
    return render(request, 'shop/post.html', context)


def contact(request):
    return render(request, 'shop/contact.html')

def about(request):
    return render(request,'shop/about.html')

