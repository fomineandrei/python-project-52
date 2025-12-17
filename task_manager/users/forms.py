from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from task_manager.users.models import User


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username'
        ]
        

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class UserUpdateForm(UserRegistrationForm):

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username
