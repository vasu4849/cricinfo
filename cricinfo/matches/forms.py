from django import forms
from .models import Match


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'

    def clean_second_team(self):
        second_team = self.cleaned_data.get('second_team')
        if(second_team is None):
            raise forms.ValidationError('Please select second team')
        return second_team

    def clean(self):
        cleaned_data = super().clean()
        first_team = cleaned_data.get('first_team')
        second_team = cleaned_data.get('second_team')
        match_status = cleaned_data.get('result')
        if first_team is None:
            raise forms.ValidationError("Please select first team")
        if second_team is None:
            raise forms.ValidationError("Please select second team")
        if first_team.name == second_team.name:
            raise forms.ValidationError('You have selected same teams. Please select different ones.')
        if match_status is None:
            raise forms.ValidationError('Please select the appropriate match status')
        if any(self.errors):
            print(self.errors)
            return self.errors
        return cleaned_data






