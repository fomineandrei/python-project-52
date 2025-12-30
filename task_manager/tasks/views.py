from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.mixins import (
    AuthRequiredMixin,
    FilterMixin,
    FormContextMixin,
    FormValidMixin,
    OwnerAccessMixin,
)
from task_manager.tasks.forms import CreateTaskForm, TasksFilterForm
from task_manager.tasks.models import Task

# Create your views here.


class IndexTasksView(AuthRequiredMixin, FilterMixin,
                     FormContextMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/index.html'
    queryset = Task.objects.order_by('id')
    filter_form = TasksFilterForm
    login_url = reverse_lazy('login_user')
    h1 = _('Задачи')
    submit_button = _('Создать Задачу')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')


class CreateTaskView(AuthRequiredMixin, FormValidMixin,
                       FormContextMixin, CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('index_tasks')
    login_url = reverse_lazy('login_user')
    success_message = _('Задача успешно создана')
    h1 = _('Создать задачу')
    submit_button = _('Создать')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(AuthRequiredMixin, FormValidMixin,
                       FormContextMixin, UpdateView):
    template_name = 'base_form.html'
    model = Task
    form_class = CreateTaskForm
    success_url = reverse_lazy('index_tasks')
    login_url = reverse_lazy('login_user')
    h1 = _('Изменение задачи')
    submit_button = _('Изменить')
    success_message = _('Задача успешно изменена')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')


class DeleteTaskView(OwnerAccessMixin, FormContextMixin, DeleteView):

    model = Task
    success_url = reverse_lazy('index_tasks')
    success_message = _('Задача успешно удалена')
    template_name = 'delete_form.html'
    h1 = _('Удаление задачи')
    submit_button = _('Да, удалить')
    not_auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')
    another_user_message = _('Задачу может удалить только ее автор')
    access_denied_redirect = reverse_lazy('index_tasks')

    def get_delete_warning(self):
        status_name = self.get_object().name
        return _(
            'Вы уверены, что хотите удалить {name}?'.format(name=status_name)
            )


class InfoTaskView(AuthRequiredMixin, FormContextMixin, DetailView):
    model = Task
    context_object_name = 'task'
    h1 = _('Просмотр задачи')
    template_name = 'tasks/detail.html'
    
