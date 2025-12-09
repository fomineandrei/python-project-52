from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView

from task_manager.users import forms, models

# Create your views here.


class IndexView(TemplateView):
    template_name = 'base.html'


class CreateUserView(CreateView):
    model = models.User
    form_class = forms.UserRegistrationForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('login_user')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        messages.success(request, self.get_form()['username'].errors)
        messages.success(request, self.get_form()['password2'].errors)
        return response


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