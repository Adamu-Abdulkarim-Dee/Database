from django import forms
from .models import SchoolBoard, Contact, User
from phonenumber_field.formfields import PhoneNumberField

class RegistrationForms(forms.Form):
    username = forms.CharField(label="Username", max_length=70,
    widget=forms.TextInput(attrs={'class':'form-control'}))

    first_name = forms.CharField(label="First Name",
    widget=forms.TextInput(attrs={'class':'form-control'}))

    last_name = forms.CharField(label="last Name",
    widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField(label="School Email",
    widget=forms.EmailInput(attrs={'class':'form-control'}))

    phone_number = PhoneNumberField(label="School Phone Number",
    widget=forms.NumberInput(attrs={'class':'form-control'}))

    password = forms.CharField(label="Password",
    widget=forms.PasswordInput(attrs={'class':'form-control'}))

    repeat_password = forms.CharField(label="Repeat Password",
    widget=forms.PasswordInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'password', 'email', 
        'first_name', 'last_name', 'phone_number', 
        'repeat_password']


class LoginForm(forms.Form):
    email = forms.EmailField(label="School Email",
    widget=forms.EmailInput(attrs={'class':'form-control'}))

    password = forms.CharField(label="Password",
    widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'password']



class EditBoardForm(forms.ModelForm):
    class Meta:
        model = SchoolBoard
        fields = ['school_name', 'p_o_box', 'school_batch', 'school_address', 'location', 'school_owner_name', 
        'tax_number']



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'