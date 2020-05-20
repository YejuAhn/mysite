from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.utils.http import is_safe_url
from django.shortcuts import redirect

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        form.save()
    return render(request, "accounts/register.html", context)


#authenticate user
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleand_data.get("password")
        user = authenticate(request, username = username, password= password)
        if user is not None:
            login(request, user)
            # if is_safe_url(redirect_path, request.get_host()):
            #     print("here")
            #     return redirect(redirect_path)
            # else:
            #     print("not safe url")
            #     return redirect("/")
            return redirect(reverse(''))
        else:
            print("error")
        return render(request, "accounts/login.html", context)


