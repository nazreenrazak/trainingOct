from django.shortcuts import render
from .models import Aktiviti
from .forms import AktivitiForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.

# Home penganjur
def home(request):
	#aktivitiid = request.GET['aktivitiid']
	# print(request.GET['aktivitiid'])

	#List of record
	var = Aktiviti.objects.all()
	# for activity in var:
	# 	print(activity.tajuk,activity.tempat,activity.penceramah)
	
	return render(request,'penganjur/home.html',{'aktiviti':var})

#update penganjur
def edit_aktiviti(request,pk):

	
	aktiviti=get_object_or_404(Aktiviti,pk=pk)
	if request.method == "POST":
		pass
		#masuk input dlm form value
		form = AktivitiForm(request.POST, instance = aktiviti)

		#check valid ke tak
		if form.is_valid():
			#save dlm variable
			aktiviti = form.save(commit=False)
			#save dlm DB
			aktiviti.save()
			return redirect(reverse_lazy('Penganjur Home'))

	else:
		form = AktivitiForm(instance = aktiviti)
	return render(request,'penganjur/editaktiviti.html', {'form': form})
# def add_aktiviti(request,pk):

# 	#add data stp kali request
# 	akt= Aktiviti(tajuk='Tajuk Baru', tempat='Tak Kesah', penceramah='Paon', hadpeserta=55)
# 	akt.save()

# 	return render(request,'penganjur/home.html')

def penganjur_new(request):

	print(request.method)

	# after klik button submit
	if request.method == "POST":
		pass
		#masuk input dlm form value
		form = AktivitiForm(request.POST)

		#check valid ke tak
		if form.is_valid():
			#save dlm variable
			aktiviti = form.save(commit=False)
			#save dlm DB
			aktiviti.save()
			messages.success(request, "Aktiviti telah dicipta ! ")
			# return redirect(reverse_lazy('add_aktiviti'))
			return redirect(reverse_lazy('Penganjur Home'))
		#if xklik button submit, just klik link sahaja
	else:
		form = AktivitiForm()
		print(form)
	return render(request,'penganjur/tambahaktiviti.html', {'form': form})
	
#delete penganjur
def delete_aktiviti(request,pk):

	#dptkan id aktivity n cari rekod
	aktvt = get_object_or_404(Aktiviti,pk=pk)

	if request.method == "POST":

		if request.POST.get("submit_yes"):
		#confirm delete
			aktvt.delete()
			return redirect(reverse_lazy('Penganjur Home'))

	return render(request,'penganjur/deleteaktiviti.html', {'aktiviti': aktvt})