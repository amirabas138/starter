from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import UserCreateForm
from .models import MyUser
from django.contrib.auth import authenticate, login,logout


def Login(request):
    if request.usre.is_authenticate:
        return redirect("shop:home")
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('login')
            # Redirect to a success page.
            ...
        else:
            return HttpResponse('false login')
            # Return an 'invalid login' error message.
            ...
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
    return render(request, 'shop/signup.html',context)

def logout_view(request):
    logout(request)
    return redirect("shop:login")

def home (request):
    return render(request,'shop/home.html')