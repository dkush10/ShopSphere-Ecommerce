from django import forms
from .models import Contact, Checkout

# class contactForm(forms.Form):
#     fname=forms.CharField(max_length=100, label='First name',widget=forms.TextInput(attrs={'placeholder':'Enter first name'}))
#     lname=forms.CharField(max_length=100, label='Last name')
#     email=forms.EmailField()
#     message=forms.CharField(max_length=500)

class contactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['fname','lname','email','message']
        exclude=['host']

class checkoutForm(forms.ModelForm):
    class Meta:
        model=Checkout
        fields=['name','email','address','city','state','zipcode','country','phone','payment','comments']
        exclude=['host']