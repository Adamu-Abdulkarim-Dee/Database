from django import forms
from .models import Primary, Science, Art, Commerce


class PrimaryForms(forms.ModelForm):
    class Meta:
        model = Primary
        fields = '__all__'

class EditPrimaryForms(forms.ModelForm):
    class Meta:
        model = Primary
        fields = '__all__'

class ScineceForms(forms.ModelForm):
    class Meta:
        model = Science
        fields = '__all__'

class EditScineceForms(forms.ModelForm):
    class Meta:
        model = Science
        fields = '__all__'

class ArtForms(forms.ModelForm):
    class Meta:
        model = Art
        fields = '__all__'

class EditArtForms(forms.ModelForm):
    class Meta:
        model = Art
        fields = '__all__'


class CommerceForms(forms.ModelForm):
    class Meta:
        model = Commerce
        fields = '__all__'

class EditCommerceForms(forms.ModelForm):
    class Meta:
        model = Commerce
        fields = '__all__'

