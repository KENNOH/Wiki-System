from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from .forms import UserSignInForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)


# Create your views here.
def handler404(request,exception):
    return render(request, 'authentication/error404.html', status=404)


def handler500(request,*args, **argv):
    return render(request, 'authentication/error500.html', status=500)


def sign_in(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            try:
                return redirect(request.GET.get('next'))
            except:
                return redirect('home')
        else:
            return render(request, 'authentication/sign_in.html', context={'form': form})
    else:
        form = UserSignInForm()
        args = {'form':form}
        args.update(csrf(request))
        return render(request, 'authentication/sign_in.html', args)


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('sign_in')