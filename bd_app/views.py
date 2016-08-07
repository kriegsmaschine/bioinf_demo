from django.shortcuts import render
from .models import Patient, ClinData, ExpData
from .forms  import *
from .utils import *

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	if request.method == 'POST':
		pt_form   = PatientForm(request.POST)

		
		clin_form = ClinDataForm(request.POST)
		#exp_form  = ExpDataForm(request.POST)
		'''
		if (pt_form.is_valid() and clin_form.is_valid() and 
			exp_form.is_valid()):
		'''

		if pt_form.is_valid():
			#process the PatientForm
			d_pt_form = processPatientForm(pt_form)
			
			#process the ClinDataForm
			#d_clin_form = processClinDataForm(clin_form)
			d_clin_form = {'empty':None}

			#process the ExpDataForm
			#d_exp_form = processExpDataForm(exp_form)
			d_exp_form = {'empty':None}

			print("inside if")
			#return the processed forms
			return render(request, 'bd_app/selection_output.html', 
				          {'ppt_form':d_pt_form, 'pclin_form':d_clin_form,'pexp_form':d_exp_form,})

	else:
		pt_form   = PatientForm()
		clin_form = ClinDataForm()
		exp_form  = ExpDataForm()

		print("inside else")

	print("never inside")
	#return the empty forms
	return render(request, 'bd_app/index.html', 
			      {'pt_form':pt_form,'clin_form':clin_form,'exp_form':exp_form,})