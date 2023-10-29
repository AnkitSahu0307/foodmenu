from django import forms
from django.contrib.auth.models import User
# why we are importing User model here is because 
#user is not actually the model which we have created , but instead it's actually inbuilt in Django.
#import UserCreation form to inherit from that particular form
from django.contrib.auth.forms import UserCreationForm 
#this class is going to inherit from UserCreationForm
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model =User
        fields =['username','email','password1','password2']
# metaclass is nothing but the class which provides informatio about the class itself