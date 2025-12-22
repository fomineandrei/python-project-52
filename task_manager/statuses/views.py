from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.mixins import (
    AuthRequiredMixin,
    FormContextMixin,
    FormValidMixin,
)
from task_manager.statuses.forms import CreateStatusForm
from task_manager.statuses.models import Status


# Create your views here.
class IndexStatusesView(AuthRequiredMixin, FormContextMixin, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'statuses/index.html'
    queryset = Status.objects.all().order_by('id')
    login_url = reverse_lazy('login_user')
    h1 = _('Статусы')
    submit_button = _('Создать статус')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')


class CreateStatusView(AuthRequiredMixin, FormValidMixin,
                       FormContextMixin, CreateView):
    model = Status
    form_class = CreateStatusForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('index_statuses')
    login_url = reverse_lazy('login_user')
    success_message = _('Статус успешно создан')
    h1 = _('Создать статус')
    submit_button = _('Создать')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')


class UpdateStatusView(AuthRequiredMixin, FormValidMixin,
                       FormContextMixin, UpdateView):
    template_name = 'base_form.html'
    model = Status
    form_class = CreateStatusForm
    success_url = reverse_lazy('index_statuses')
    login_url = reverse_lazy('login_user')
    h1 = _('Изменение татуса')
    submit_button = _('Изменить')
    success_message = _('Статус успешно изменен')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')
    

class DeleteStatusView(AuthRequiredMixin, FormContextMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('index_statuses')
    success_message = _('Статус успешно удален')
    template_name = 'delete_form.html'
    h1 = _('Удаление статуса')
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
            messages.success(request, _('Статус успешно удален'))
            return response
        except ProtectedError:
            messages.error(request,
                    _('Невозможно удалить статус, потому что он используется'))
            return redirect('index_statuses')
        except Exception as e:
            messages.error(request, e)
            return redirect('index_statuses')
