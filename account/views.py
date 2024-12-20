from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from account.forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from account.models import Profile


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             user = authenticate(username=cleaned_data['username'],
#                                 password=cleaned_data['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse("Uwierzytelnianie zokończyło się sukcesem")
#                 else:
#                     return HttpResponse("Konto zablokowane")
#             else:
#                 return HttpResponse("Nieprawidłowe dane logowania")
#     else:
#         form = LoginForm()
#     return render(request,'account/login.html', {'form': form})
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',{'user_form':user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_name = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_name.is_valid():
            user_form.save()
            profile_name.save()
            messages.success(request,"pomyslnie zaktualizowano konto")
        else:
            messages.error(request,"nie mozna zaktualizowa konta")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_name = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',
                  {'user_form':user_form,'profile_name':profile_name})