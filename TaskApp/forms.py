from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Register, Task


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Register
        fields = ['username', 'email', 'password1', 'password2']






class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
