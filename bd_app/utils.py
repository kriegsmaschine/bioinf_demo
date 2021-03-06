from bd_app.models import *



'''
function to convert a LIST of a QuerySet to a list
Use this function to take PatientForm QuerySet and
convert it to a list of integers for the patients'
ForeignKeys id's
'''
def convertMultListQuerySet(id_queryset):

	id_list = []
	for values in id_queryset:
		for elements in values:
			id_list.append(elements)

	return id_list

'''
function to convert a QuerySet to a list
Use this function to take PatientForm QuerySet and
convert it to a list of integers for the patients'
ForeignKeys id's
'''
def convertSingleListQuerySet(id_queryset):
	id_list = []
	for values in id_queryset:
		id_list.append(values)

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

	id_queryset = []
	id_queryset.append(Patient.objects.filter(cohort__in=pt_form['cohort'].value(),
				   gender__in=pt_form['gender'].value()).values_list('id',flat=True))

	id_list = convertMultListQuerySet(id_queryset)

	return id_list




'''
Function to perform database query on pt_keys from PatientForm()
AND the user input selections from the Clinical Parameters
'''
def processClinDataForm(clin_form, pt_key):
	'''
	Function to process clin_form and perform querysets on form
	parameters and the returned pt_keys from the pt_form
	'''



	'''
	use this line and following IF statement when need to test 
	if a selection was made run a queryset using the POST form 
	if ot data was submitted then the length of the QuerySet will == 0
	'''
	check_msi_len = ClinData.objects.filter(msi__in=clin_form['msi'].value())

	if len(check_msi_len) < 1:
		clin_form.msi = ['mss','msi-h','msi-l',]
		msi_selection = clin_form.msi
	else:
		msi_selection = clin_form['msi'].value()

	'''
	use this line to check if any path_stages were chosen
	if a selection was made run a queryset using the POST form
	if no data was submitted then the length of the QuerySet will == 0

	'''
	check_pStage_len = ClinData.objects.filter(path_stage__in=clin_form['path_stage'].value())

	if len(check_pStage_len) < 1:
		clin_form.path_stage = ['-1','1','2','3','4']
		pStage_selection = clin_form.path_stage
	else:
		pStage_selection = clin_form['path_stage'].value()


	'''
	This is the QuerySet to filter on all clinical parameters
	'''
	id_queryset = []


	'''
	use this IF statement to check if a selection was made for 'days_to_death'
	if no selection was made then select all values in the database
	if a selection is made, pass on list of selection values to query
	'''
	if (len(ClinData.objects.filter(days_to_death__in=clin_form['days_to_death'].value())) < 1 or 
		   (clin_form['dtd_radio'].value() == 1)):
		dtd_selection = convertMultListQuerySet(ClinData.objects.values_list('days_to_death'))
		id_queryset = ClinData.objects.filter(id__in=pt_key, msi__in=msi_selection,
		              days_to_death__in=dtd_selection, path_stage__in=pStage_selection). \
			          values_list('id',flat=True)

	else:
		#convert list to integer; get first element of list
		dtd_selection = clin_form['days_to_death'].value()
		dtd_selection = dtd_selection[0]

		#if > (greater than) days to death is chosen
		if clin_form['dtd_radio'].value() == 2:
			id_queryset = ClinData.objects.filter(id__in=pt_key, msi__in=msi_selection,
		                  days_to_death__gt=dtd_selection, path_stage__in=pStage_selection). \
			              values_list('id',flat=True)

		#if < (less than) days to death is chosen 
		else:
			id_queryset = ClinData.objects.filter(id__in=pt_key, msi__in=msi_selection,
		                  days_to_death__lt=dtd_selection, path_stage__in=pStage_selection). \
			              values_list('id',flat=True)			


	if id_queryset == None:
		#if filter returns no items in the QuerySet then search by pt_key from 
		#the PatientForm()
		id_list = pt_key
	else:
		id_list = convertSingleListQuerySet(id_queryset)

	#may remove {'msival':msi_selection} from return dictionary, used for testing purposes
	dict_clinData = {'id_list':id_list}

	return dict_clinData



'''
Function to retreive expression data by pt_keys from PatientForm()
AND ClinDataForm()  also from user selections in the
Gene of Interest
'''
def processExpDataForm(exp_form, chart_form, pt_key):

	gene_selection = exp_form['genes'].value()[0]
	pt_key_list = convertMultListQuerySet(pt_key.values())

	exp_data = ExpData.objects.filter(id__in=pt_key_list).values_list(gene_selection, flat=True)

	exp_data = convertSingleListQuerySet(exp_data)

	plot_selection = chart_form['chartType'].value()
	exp_data = {'exp_data':exp_data, 'plot':plot_selection, 'gene':gene_selection,}

	return exp_data


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