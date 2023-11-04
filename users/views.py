from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreateForm, UserUpdateForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            'form':create_form
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()

            #create user accaunt
            return redirect('users:login')

        else:
            context = {
                'form': create_form
            }
            return render(request, 'users/register.html', context)

class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'users/login.html', {"login_form":login_form})

    def post(self, request):
        login_form = AuthenticationForm(data = request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'Siz tizimga kirdingiz!')

            return redirect('books:list')
        else:
            return render(request, 'users/login.html', {"login_form": login_form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html', {'user': request.user})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'Siz tizimdan chiqdingiz!')
        return redirect('landing_page')

class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request, 'users/profile_edit.html', {'form': user_update_form})

    def post(self, request):
        name = request.POST['first_name']

        user_update_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES,
        )
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, 'Profil ma\'lumotlari yangilandi!')

            return redirect('users:profile')

        return render(request, 'users/profile_edit.html', {'form': user_update_form})
