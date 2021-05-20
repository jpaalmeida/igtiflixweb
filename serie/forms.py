from django import forms
from serie.models import Serie
from django.core.exceptions import ValidationError

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'

    def clean_description(self):
        des = self.cleaned_data['nome']
        if des == None:
            raise ValidationError("Description cannot be empty")
        return des