from django import forms
from .models import Primary, Secondary
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

class PrimaryForms(forms.ModelForm):
    signature_of_student = JSignatureField(
        widget=JSignatureWidget(
            jsignature_attrs={'color':'#e0b642', 'height':'200px'}
            )
            )
    
    signature_of_guardian = JSignatureField(
        widget=JSignatureWidget(
            jsignature_attrs={'color':'#e0b642', 'height':'200px'}
            )
            )
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Primary
        fields = ['admission_number', 'profile_picture', 'first_name', 
        'last_name', 'gender', 'address_of_student', 'class_Of_student', 
        'comment_of_student', 'year_of_graduation', 'date_of_birth', 'religion', 'mother_name', 'signature_of_student', 
        'nationality_of_student', 'state_of_student', 'local_government_of_student','certificate_of_birth_photo', 
        'residential_certificate_photo', 'name_of_guardian', 'phone_number', 
        'address_of_guardian', 'nationality_of_guardian', 'occupation_of_guardian', 'work_address',
        'state_of_guardian', 'local_government_of_guardian', 'relationship', 'signature_of_guardian']

        

class SecondaryForm(forms.ModelForm):
    signature_of_student = JSignatureField(
        widget=JSignatureWidget(
            jsignature_attrs={'color':'#e0b642', 'height':'200px'}
            )
            )
    signature_of_guardian = JSignatureField(
        widget=JSignatureWidget(
            jsignature_attrs={'color':'#e0b642', 'height':'200px'}
            )
            )
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Secondary
        fields = ['admission_number', 'profile_picture', 'first_name', 
        'last_name', 'gender', 'address_of_student', 'class_Of_student', 
        'comment_of_student', 'year_of_graduation', 'date_of_birth', 'religion', 'mother_name', 'signature_of_student', 
        'nationality_of_student', 'state_of_student', 'local_government_of_student','certificate_of_birth_photo', 
        'residential_certificate_photo', 'name_of_guardian', 'phone_number', 
        'address_of_guardian', 'nationality_of_guardian', 'occupation_of_guardian', 'work_address',
        'state_of_guardian', 'local_government_of_guardian', 'relationship', 'signature_of_guardian']

        

#This side is for editing
class EditSecondaryForm(forms.ModelForm):
    signature_of_student = JSignatureField(
        widget=JSignatureWidget(
            jsignature_attrs={'color':'#e0b642', 'height':'200px'}
            )
            )
    signature_of_guardian = JSignatureField(
        widget=JSignatureWidget(
            jsignature_attrs={'color':'#e0b642', 'height':'200px'}
            )
            )
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Secondary
        fields = ['admission_number', 'profile_picture', 'first_name', 
        'last_name', 'gender', 'address_of_student', 'class_Of_student', 
        'comment_of_student', 'year_of_graduation', 'date_of_birth', 'religion', 'mother_name', 'signature_of_student', 
        'nationality_of_student', 'state_of_student', 'local_government_of_student','certificate_of_birth_photo', 
        'residential_certificate_photo', 'name_of_guardian', 'phone_number', 
        'address_of_guardian', 'nationality_of_guardian', 'occupation_of_guardian', 'work_address',
        'state_of_guardian', 'local_government_of_guardian', 'relationship', 'signature_of_guardian']

class PrimaryEditForms(forms.ModelForm):
    signature_of_student = JSignatureField(
        widget=JSignatureWidget(
            jsignature_attrs={'color':'#e0b642', 'height':'200px'}
            )
            )
    
    signature_of_guardian = JSignatureField(
        widget=JSignatureWidget(
            jsignature_attrs={'color':'#e0b642', 'height':'200px'}
            )
            )
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Primary
        fields = ['admission_number', 'profile_picture', 'first_name', 
        'last_name', 'gender', 'address_of_student', 'class_Of_student', 
        'comment_of_student', 'year_of_graduation', 'date_of_birth', 'religion', 'mother_name', 'signature_of_student', 
        'nationality_of_student', 'state_of_student', 'local_government_of_student','certificate_of_birth_photo', 
        'residential_certificate_photo', 'name_of_guardian', 'phone_number', 
        'address_of_guardian', 'nationality_of_guardian', 'occupation_of_guardian', 'work_address',
        'state_of_guardian', 'local_government_of_guardian', 'relationship', 'signature_of_guardian']





