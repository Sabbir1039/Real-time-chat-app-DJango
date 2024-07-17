from django.shortcuts import render, redirect
from usersapp.models import CustomUser
from django.contrib import messages
from usersapp.forms import UserRegistrationForm, UserUpdateForm
from django.views import generic

# class HomeView(generic.TemplateView):
#     template_name = "usersapp/home.html"
    
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Successfully account created for {username}")
            return redirect('login')
            
        else:
            messages.error(request,'Error! Can not create account. Try agin!')
            return redirect('register')
            
    context = {
        "forms": UserRegistrationForm(),
        "title": "Register"
    }
    return render(request, "usersapp/register.html", context)

def user_profile(request):
    if request.method == "POST":
        profile_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            messages.error(request, f'Your account can not be updated!')
            return redirect('profile')
    else:
        context = {
            "p_form": UserUpdateForm(instance=request.user)
        }
        return render(request, 'usersapp/profile.html', context)