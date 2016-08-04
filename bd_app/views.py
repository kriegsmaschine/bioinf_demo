from django.shortcuts import render
from .models import Patient, ClinData, ExpData
from .forms  import *

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	if request.method == 'POST':
		pt_form   = PatientForm(request.POST)
		clin_form = ClinDataForm(request.POST)
		exp_form  = ExpDataForm(request.POST)

		if pt_form.is_valid() and clin_form.is_valid() and 
		   exp_form.is_valid():



	else:
		pt_form   = PatientForm()
		clin_form = ClinDataForm()
		exp_form  = ExpDataForm()