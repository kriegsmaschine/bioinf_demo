from django import forms
from .models import Patient, ClinData, ExpData

from django.contrib.admin.widgets import FilteredSelectMultiple

class PatientForm(forms.ModelForm):
	class Meta:
		model  = Patient
		fields = ('cohort','gender')

class ClinDataForm(forms.ModelForm):
	class Meta:
		model  = ClinData
		fields = (
			      'msi','vital_status','days_to_death',
		          'days_to_last_followup','path_stage',
			     )

class ExpDataForm(forms.ModelForm):
	class Meta:
		model = ExpData
		fields = (
                   'braf','brap','brca1','brca2','brcc3',
                   'brd1','brd2','brd3','brd4',
			     )

class TestForm(forms.Form):

	cohort = forms.MultipleChoiceField(choices=[], required=False)

	def __init__(self, *args, **kwargs):
		super(TestForm, self).__init__(*args, **kwargs)
		self.fields['cohort'].choices = Patient.objects.all().values_list('cohort','cohort').distinct()