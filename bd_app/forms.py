from django import forms
from .models import Patient, ClinData, ExpData

class PatientForm(forms.ModelForm):
	class Meta:
		model  = Patient
		fields = ('cohort','gender')

class ClinDataForm(forms.ModelForm):
	class Meta:
		model  = ClinData
		fields = (
			      'msi','vital_status','days_to_death',
		          'days_to_followup','path_stage',
			     )

class ExpDataForm(forms.ModelForm):
	class Meta:
		model = ExpData
		fields = (
                   'braf','brap','brca1','brca2','brcc3',
                   'brd1','brd2','brd3','brd4',
			     )