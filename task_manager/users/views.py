from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.mixins import (
    FormContextMixin,
    FormValidMixin,
    OwnerAccessMixin,
)
from task_manager.users import forms, models

# Create your views here.


class IndexView(FormContextMixin, ListView):
    model = models.User
    context_object_name = 'users'
    template_name = 'users/index.html'
    queryset = models.User.objects.all().order_by('id')
    h1 = _('Пользователи')


class CreateUserView(FormContextMixin, FormValidMixin, CreateView):
    model = models.User
    form_class = forms.UserRegistrationForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('login_user')
    success_message = _('Пользователь успешно зарегистрирован')
    h1 = _('Регистрация')
    submit_button = _('Зарегистрировать')


class UpdateUserView(OwnerAccessMixin, FormContextMixin,
                     FormValidMixin, UpdateView):
    template_name = 'base_form.html'
    model = models.User
    form_class = forms.UserUpdateForm
    success_url = reverse_lazy('index_users')
    access_denied_redirect = reverse_lazy('index_users')
    h1 = _('Изменение пользователя')
    submit_button = _('Изменить')
    success_message = _('Пользователь успешно изменен')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')
    another_user_message = _(
        'У вас нет прав для изменения другого пользователя.'
        )


class DeleteUserView(OwnerAccessMixin, FormContextMixin, DeleteView):
    model = models.User
    success_url = reverse_lazy('index_users')
    access_denied_redirect = reverse_lazy('index_users')
    template_name = 'delete_form.html'
    h1 = _('Удаление пользователя')
    submit_button = _('Да, удалить')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')
    another_user_message = _(
        'У вас нет прав для изменения другого пользователя.'
        )

    def get_delete_warning(self):
        full_name = self.get_object().get_full_name()
        return _(
            'Вы уверены, что хотите удалить {name}?'.format(name=full_name)
            )
    
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(request, _('Пользователь успешно удален'))
            return response
        except ProtectedError:
            messages.error(request,
                _('Невозможно удалить пользователя,'
                ' потому что он используется'))
            return redirect('index_users')
        except Exception as e:
            messages.error(request, e)
            return redirect('index_users')


class LoginUserView(FormContextMixin, FormValidMixin, LoginView):
    form_class = forms.UserLoginForm
    template_name = 'base_form.html'
    next_page = reverse_lazy('index')
    app_index_url = reverse_lazy('index_users')
    success_message = _('Вы залогинены')
    h1 = _('Вход')
    submit_button = _('Войти')


class LogoutUserView(FormValidMixin, LogoutView):
    next_page = reverse_lazy('index')
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        messages.info(self.request, _('Вы разлогинены'))
        return response
