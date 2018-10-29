from django.shortcuts import render
from .models import Aktiviti
from .forms import AktivitiForm

# Create your views here.

# Home penganjur
def home(request):
	#aktivitiid = request.GET['aktivitiid']
	print(request.GET['aktivitiid'])

	#List of record
	var = Aktiviti.objects.all()
	for activity in var:
		print(activity.tajuk,activity.tempat,activity.penceramah)
	
	return render(request,'penganjur/home.html')

#update penganjur
def update_penganjur(request,pk):

	#update data stp kali request
	aktiviti=get_object_or_404(Aktiviti,pk)
	aktiviti= Aktiviti(tajuk='Tajuk lagi Baru', tempat='Tak Kesah', penceramah='Paon', hadpeserta=55)
	aktiviti.save()

	return render(request,'penganjur/home.html')

def add_aktiviti(request,pk):

	#add data stp kali request
	akt= Aktiviti(tajuk='Tajuk Baru', tempat='Tak Kesah', penceramah='Paon', hadpeserta=55)
	akt.save()

	return render(request,'penganjur/home.html')

def penganjur_new(request):

	print(request.method)
	if request.method == "POST":
		pass
	else:
		form = AktivitiForm()

	return render(request,'penganjur/tambahaktiviti.html', {'form': form})
	
#delete penganjur
def delete_penganjur(request,pk):

	#dptkan id aktivity n cari rekod
	aktvt = get_object_or_404(Aktiviti,pk)

	#confirm delete
	aktvt.delete()
	return render(request,'penganjur/home.html')