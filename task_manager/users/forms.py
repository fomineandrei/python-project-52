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
    
    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 == '111':
            self.add_error('password2', ValidationError('Password2Error'))
        return password2
    
    def clean(self):
        return super().clean()
        

class UserLoginForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
