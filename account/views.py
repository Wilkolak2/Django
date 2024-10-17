from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from account.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'],
                                password=cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Uwierzytelnianie zokończyło się sukcesem")
                else:
                    return HttpResponse("Konto zablokowane")
            else:
                return HttpResponse("Nieprawidłowe dane logowania")
    else:
        form = LoginForm()
    return render(request,'account/login.html', {'form': form})
