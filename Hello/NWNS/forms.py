from django import forms
from .models import College , University, StandaloneInstitution

class Index(forms.ModelForm):
    class Meta:
        model = College
        fields = ('name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].queryset = name.objects.none()