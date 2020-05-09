from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "name", "surname", "obligation", "assigned_function", "location", "password1", "password2"]
