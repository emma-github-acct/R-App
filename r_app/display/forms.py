from django import forms

from display.models import ReportFlag

class ReportFlagForm(forms.ModelForm):
    
    class Meta:
        model = ReportFlag
        fields = ('location', 'description',)