from bd_app.models import *



'''
function to convert a QuerySet to a list
Use this function to take PatientForm QuerySet and
convert it to a list of integers for the patients'
ForeignKeys id's
'''
def convertQuerySetToList(id_queryset):

	id_list = []
	for values in id_queryset:
		for elements in values:
			id_list.append(elements)

	return id_list


'''
function to take user selection from PatientDataForm and
generate a QuerySet of ForeignKeys to pass on to the 
ClinDataForm
'''
def processPatientForm(pt_form):
	'''
	Function to process pt_form input to query database to
	return patient ID keys for the query set based on 
	SELECT cohort, gender

	SELECT pt_id WHERE cohort like '' AND gender like ''
	'''

	id_queryset.append(Patient.objects.filter(cohort__in=pt_form['cohort'].value(),
				   gender__in=pt_form['gender'].value()).values_list('id',flat=True))

	id_list = convertQuerySetToList(id_queryset)

	return id_list



def processClinDataForm(clin_form, pt_key):
	'''
	Function to process clin_form and perform querysets on form
	parameters and the returned pt_keys from the pt_form
	'''

	pt_queryset = ClinData.objects.filter(id__in=pt_key, msi__in=clin_form['msi'].value()). \
			      values_list('id',flat=True)

	pt_list = convertQuerySetToList(pt_queryset)

	return pt_list



def processExpDataForm(exp_form):
	return exp_form



'''
Fucntion to take in ch = ExpData._meta.get_fields() and convert
genes list to dictionary and then convert dictionary to 
2-tuple to set dynamic fields choices 'genes' for ExpDataForm
'''
def convertMetaFieldsToList(ch):
	ch_genes = []

	#get genes names in list
	for c in ch:
		ch_genes.append(c.name)

	ch_genes.remove('id')
	ch_genes.remove('patient')

	#convert gene list to dictionary
	z = dict((x,x) for x in ch_genes)

	#convert dictionary to 2-tuple 
	tch_genes = [(v,k) for k, v in z.items()]

	return tch_genes