from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Task(models.Model):
    name = models.CharField(_('имя'), max_length=150, unique=True)
    description = models.TextField(_('описание'), blank=True)
    author = models.ForeignKey('users.User',
                                related_name='author',
                                on_delete=models.PROTECT,
                                verbose_name=_('автор'),
                                null=True)
    executor = models.ForeignKey('users.User',
                                 related_name='executor',
                                 on_delete=models.PROTECT,
                                 blank=True,
                                 null=True,
                                 verbose_name=_('исполнитель'))
    status = models.ForeignKey('statuses.Status',
                               on_delete=models.PROTECT,
                               verbose_name=_('статус'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
