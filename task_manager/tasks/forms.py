from django.forms import Form, ModelForm
from django.forms.fields import BooleanField, ChoiceField
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Task


class CreateTaskForm(ModelForm):
     
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class TasksFilterForm(Form):
    default = (None, '-----------')
    status_choices = [default] + \
        [(status.id, status) for status in Task.status.get_queryset()]
    executor_choices = [default] + \
        [(executor.id, executor) for executor in Task.executor.get_queryset()]
    labels_choices = [default] + \
        [(lab.id, lab) for lab in Task.labels.through.label.get_queryset()]
    
    status = ChoiceField(choices=status_choices,
                         label=_('Статус'), required=False)
    executor = ChoiceField(choices=executor_choices,
                         label=_('Исполнитель'), required=False)
    author_id = BooleanField(label=_('Только мои задачи'), required=False)
    labels = ChoiceField(choices=labels_choices,
                         label=_('Метка'), required=False)

