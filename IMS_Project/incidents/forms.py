from django import forms 
from .models import Contact

class PersonForm(forms.Form):
    name=forms.CharField(max_length=50,label='Enter your name',initial='John',label_suffix=':::::::::')
    age=forms.IntegerField(label='Enter your Age')
    gender=forms.CharField(widget=forms.RadioSelect,required=False)
    email=forms.EmailField(help_text='Type email with .com')
    password=forms.CharField(widget=forms.PasswordInput)
    describe=forms.CharField(widget=forms.Textarea)
    birthdate=forms.DateField(widget=forms.SelectDateWidget)
    
class ContactForm(forms.ModelForm):
    
    class Meta:
        model=Contact
        fields='__all__'

    