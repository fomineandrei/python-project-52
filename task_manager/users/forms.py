from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ValidationError

from task_manager.users.models import User


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username'
        ]

    def clean_username(self):
        raise ValidationError('!!!!!!!!!!!!!!!!!!!')
        return super().clean()
    

class UserLoginForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
