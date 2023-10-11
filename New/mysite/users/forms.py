from django import forms
from django.contrib.auth.models import User
# why we are importing user model from here is because
# User is not actually the model which we have created, but instead it's actually inbuilt into Django.
#import user creation form to inherit from thst particular form
from django.contrib.auth.forms import UserCreationForm 
#this class is going to inherit from UCF
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
#a metaclass is nothing but the class which provides information about this class itself.
