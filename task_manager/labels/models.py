# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Label(models.Model):
    name = models.CharField(_('name'), max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
