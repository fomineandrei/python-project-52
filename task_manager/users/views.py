from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView, View

from task_manager.users import forms, models

# Create your views here.


class IndexView(TemplateView):
    template_name = 'base.html'


class CreateUserView(View):

    def get(self, request):
        form = forms.UserRegistrationForm()
        return render(
            request,
            'users/create_user.html',
            context={'form': form}
        )
    
    def post(self, request, *args, **kwargs):
        model = models.User()
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            model.first_name = form.cleaned_data['first_name']
            model.last_name = form.cleaned_data['last_name']
            model.username = form.cleaned_data['username']
            model.set_password(form.cleaned_data['password'])
            model.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('login_user')
        return render(
            request,
            'users/create_user.html',
            context={'form': form}
        )
    

class UpdateUserView(TemplateView):
    pass


class DeleteUserView(TemplateView):
    pass


class LoginUserView(View):

    def get(self, request, *args, **kwargs):
        form = forms.UserLoginForm()
        return render(
            request,
            'users/create_user.html',
            context={'form': form}
        )


class LogoutUserView(TemplateView):
    pass