from django.forms import ModelForm
from django import forms
from .models import Case, CaseUpdate


class CaseUpdateForm(ModelForm):
    class Meta:
        model = CaseUpdate
        fields = ['update_description', 'case']
        # user does not manually select which case a case update is for
        labels = {'update_description': ""}
        widgets = {'case': forms.HiddenInput()}

    def save(self, commit=True):
        case_update = super().save()
        case_update.case.last_updated = case_update.creation_date
        case_update.case.save()
        case_update.save()
        return case_update


class IntakeForm(ModelForm):
    class Meta:
        model = Case
        fields = ['divisions', 'client_name',
                  'client_email', 'client_phone', 'client_SID',
                  'incident_description']