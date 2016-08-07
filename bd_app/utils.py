def processPatientForm(pt_form):
	return {'cohort':pt_form['cohort'].value(),
	        'gender':pt_form['gender'].value(),}

def processClinDataForm(clin_form):
	return clin_form

def processExpDataForm(exp_form):
	return exp_form