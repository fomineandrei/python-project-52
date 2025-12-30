from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.labels.forms import CreateLabelForm
from task_manager.labels.models import Label
from task_manager.mixins import (
    AuthRequiredMixin,
    FormContextMixin,
    FormValidMixin,
)


# Create your views here.
class IndexLabelsView(AuthRequiredMixin, FormContextMixin, ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'labels/index.html'
    queryset = Label.objects.all().order_by('id')
    login_url = reverse_lazy('login_user')
    h1 = _('Метки')
    submit_button = _('Создать метку')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')


class CreateLabelView(AuthRequiredMixin, FormValidMixin,
                       FormContextMixin, CreateView):
    model = Label
    form_class = CreateLabelForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('index_labels')
    login_url = reverse_lazy('login_user')
    success_message = _('Метка успешно создана')
    h1 = _('Создать метку')
    submit_button = _('Создать')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')


class UpdateLabelView(AuthRequiredMixin, FormValidMixin,
                       FormContextMixin, UpdateView):
    template_name = 'base_form.html'
    model = Label
    form_class = CreateLabelForm
    success_url = reverse_lazy('index_labels')
    login_url = reverse_lazy('login_user')
    h1 = _('Изменение метки')
    submit_button = _('Изменить')
    success_message = _('Метка успешно изменена')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')
    

class DeleteLabelView(AuthRequiredMixin, FormContextMixin, DeleteView):
    model = Label
    success_url = reverse_lazy('index_labels')
    success_message = _('Метка успешно удалена')
    template_name = 'delete_form.html'
    h1 = _('Удаление метки')
    submit_button = _('Да, удалить')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')

    def get_delete_warning(self):
        status_name = self.get_object().name
        return _(
            'Вы уверены, что хотите удалить {name}?'.format(name=status_name)
            )
    
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(request, _('Метка успешно удалена'))
            return response
        except ProtectedError:
            messages.error(request,
                _('Невозможно удалить метку, потому что она используется'))
            return redirect('index_labels')
        except Exception as e:
            messages.error(request, e)
            return redirect('index_labels')
