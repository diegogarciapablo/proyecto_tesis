from django.shortcuts import render, redirect
from .form_lugar import FormLugar, FormSchool, FormChurch, FormLodgings, FormSquare, FormRestaurant

def paso1(request):
	return render(request,'crud/choice_add.html')


def AñadirLugar(request):
	if request.method == 'POST':
		flugar=FormLugar(request.POST)
		rec_lug= request.POST.get('tipo')
		if flugar.is_valid():
			flugar.save()
			if(rec_lug=='colegio'):
				return redirect('AColegio/')
			if (rec_lug=='plaza'):
				return redirect('square/')
			if (rec_lug=='iglesia'):
				return redirect('church/')
			if (rec_lug=='restaurante'):
				return redirect('restaurant/')
			if (rec_lug=='alojamiento'):
				return redirect('lodgings/')
	else:
		flugar=FormLugar()
	return render(request,'formLugar.html', {'flugar': flugar})
		

def CrearColegio(request):
	if request.method=='POST':
		var_cole= FormSchool(request.POST)
		if var_cole.is_valid():
			var_cole.save()
			return redirect(index)
	else:
		var_cole = FormSchool()
	return render(request,'crud/lugares/form_colegio.html',{'var_cole': var_cole})


def CrearIglesia(request):
	if request.method=='POST':
		var_iglesia=FormChurch(request.POST)
		if var_iglesia.is_valid():
			var_iglesia.save()
			return redirect(index)
	else:
		var_iglesia=FormChurch()
	return render(request,'crud/lugares/form_iglesia.html',{'var_iglesia': var_iglesia})



def CrearAlojamiento(request):
	if request.method=='POST':
		var_alojamiento=FormLodgings(request.POST)
		if var_alojamiento.is_valid():
			var_alojamiento.save()
			return redirect(index)
	else:
		var_alojamiento=FormLodgings()
	return render(request,'crud/lugares/form_alojamiento.html',{'var_alojamiento': var_alojamiento})


def CrearPlaza(request):
	if request.method=='POST':
		var_plaza=FormSquare(request.POST)
		if var_plaza.is_valid():
			var_plaza.save()
			return redirect(index)
	else:
		var_plaza=FormSquare()
	return render(request,'crud/lugares/form_plaza.html',{'var_plaza': var_plaza})

def CrearRestaurante(request):
	if request.method=='POST':
		var_restau=FormRestaurant(request.POST)
		if var_restau.is_valid():
			var_restau.save()
			return redirect(index)
	else:
		var_restau=FormRestaurant()
	return render(request,'crud/lugares/form_restaurante.html',{'var_restau': var_restau})