from django.apps import apps
from django.forms import Form, ModelForm
from django.forms.fields import BooleanField, ChoiceField
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Task

Status = apps.get_model('statuses.Status')
Label = apps.get_model('labels.Label')
User = apps.get_model('users.User')


class CreateTaskForm(ModelForm):
     
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class TasksFilterForm(Form):

    default = (None, '-----------')
    
    status = ChoiceField(
        choices=[default], label=_('Статус'), required=False)
    executor = ChoiceField(
        choices=[default], label=_('Исполнитель'), required=False)
    labels = ChoiceField(
        choices=[default], label=_('Метка'), required=False)
    author_id = BooleanField(
        label=_('Только мои задачи'), required=False)
  
    def update_choices(self):
        self.fields['status'].choices = [self.default] + \
            [(status.id, status) for status in Status.objects.all()]
        self.fields['executor'].choices = [self.default] + \
            [(executor.id, executor) for executor in User.objects.all()]
        self.fields['labels'].choices = [self.default] + \
            [(label.id, label) for label in Label.objects.all()]
