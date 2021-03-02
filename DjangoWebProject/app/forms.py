"""
Definition of forms.
"""

from django import forms
from .models import student, teacher
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

  
  
# creating a form 
class studentForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = student 
  
        # specify fields to be used 
        fields = [ 
            "studant_name", "college", "phone", "email"] 



# creating a form 
class teacherForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = teacher 
  
        # specify fields to be used 
        fields = [ 
            "teach_name", "college", "phone", "email"] 
