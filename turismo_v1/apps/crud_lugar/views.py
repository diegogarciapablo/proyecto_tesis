from django.shortcuts import render, redirect
from .form_lugar import FormLugar, FormSchool, FormChurch, FormLodgings, FormSquare, FormRestaurant, FormEvento, FormFoto
from .models import colegio, iglesia, plaza, restaurante, alojamiento, evento, foto, admin_agregar
from  django.core.exceptions import ObjectDoesNotExist

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
			return redirect('index')
	else:
		var_cole = FormSchool()
	return render(request,'crud/lugares/form_colegio.html',{'var_cole': var_cole})


def CrearIglesia(request):
	if request.method=='POST':
		var_iglesia=FormChurch(request.POST)
		if var_iglesia.is_valid():
			var_iglesia.save()
			message="Lugar Iglesia creado exitosamente"
			return redirect('index')
	else:
		var_iglesia=FormChurch()
	return render(request,'crud/lugares/form_iglesia.html',{'var_iglesia': var_iglesia})



def CrearAlojamiento(request):
	if request.method=='POST':
		var_alojamiento=FormLodgings(request.POST)
		if var_alojamiento.is_valid():
			var_alojamiento.save()
			return redirect('index')
	else:
		var_alojamiento=FormLodgings()
	return render(request,'crud/lugares/form_alojamiento.html',{'var_alojamiento': var_alojamiento})


def CrearPlaza(request):
	if request.method=='POST':
		var_plaza=FormSquare(request.POST)
		if var_plaza.is_valid():
			var_plaza.save()
			return redirect('index')
	else:
		var_plaza=FormSquare()
	return render(request,'crud/lugares/form_plaza.html',{'var_plaza': var_plaza})

def CrearRestaurante(request):
	if request.method=='POST':
		var_restau=FormRestaurant(request.POST)
		if var_restau.is_valid():
			var_restau.save()
			return redirect('index')
	else:
		var_restau=FormRestaurant()
	return render(request,'crud/lugares/form_restaurante.html',{'var_restau': var_restau})



def ListarColegio(request):
	c_lista = colegio.objects.all() 
	return render(request,'crud/listar_colegio.html',{'c_lista': c_lista})


def ListarIglesia(request):
	i_lista = iglesia.objects.all() 
	return render(request,'crud/listar_iglesia.html',{'i_lista': i_lista})


def ListarRestaurante(request):
	r_lista = restaurante.objects.all() 
	return render(request,'crud/listar_restaurante.html',{'r_lista': r_lista})


def ListarPlaza(request):
	p_lista = plaza.objects.all() 
	return render(request,'crud/listar_plaza.html',{'p_lista': p_lista})


def ListarAlojamiento(request):
	a_lista = alojamiento.objects.all() 
	return render(request,'crud/listar_alojamiento.html',{'a_lista': a_lista})





def EditarColegio(request, cod_colegio):
	var_cole= None
	error = None
	try:
		e_colegio = colegio.objects.get(cod_colegio=cod_colegio)
		if request.method == 'GET':
			var_cole = FormSchool(instance = e_colegio)
		else:
			var_cole= FormSchool(request.POST, instance = e_colegio)
			if var_cole.is_valid():
				var_cole.save()
			return redirect('index')
	except ObjectDoesNotExist as e:
		error = e
	return render(request, 'crud/lugares/form_colegio.html',{'var_cole': var_cole, 'error': error})

def EditarIglesia(request, cod_iglesia):
	var_iglesia=None
	error=None
	try:
		e_iglesia = iglesia.objects.get(cod_iglesia=cod_iglesia)
		if request.method == 'GET':
			var_iglesia = FormChurch(instance = e_iglesia)
		else:
			var_iglesia=FormChurch(request.POST, instance = e_iglesia)
			if var_iglesia.is_valid():
				var_iglesia.save()
			return redirect('index')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'crud/lugares/form_iglesia.html', {'var_iglesia': var_iglesia, 'error': error})



def EditarAlojamiento(request, cod_alojamiento):
	var_alojamiento=None
	error=None
	try:
		e_alojamiento = alojamiento.objects.get(cod_alojamiento=cod_alojamiento)
		if request.method == 'GET':
			var_alojamiento = FormLodgings(instance = e_alojamiento)
		else:
			var_alojamiento=FormLodgings(request.POST, instance = e_alojamiento)
			if var_alojamiento.is_valid():
				var_alojamiento.save()
			return redirect('index')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'crud/lugares/form_alojamiento.html', {'var_alojamiento': var_alojamiento, 'error': error})


def EditarPlaza(request, cod_plaza):
	var_plaza=None
	error=None
	try:
		e_plaza = plaza.objects.get(cod_plaza=cod_plaza)
		if request.method == 'GET':
			var_plaza = FormSquare(instance = e_plaza)
		else:
			var_plaza=FormSquare(request.POST, instance = e_plaza)
			if var_plaza.is_valid():
				var_plaza.save()
			return redirect('index')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'crud/lugares/form_plaza.html', {'var_plaza': var_plaza, 'error': error})



def EditarRestaurante(request, cod_restaurante):
	var_restau=None
	error=None
	try:
		e_restaurante = restaurante.objects.get(cod_restaurante=cod_restaurante)
		if request.method == 'GET':
			var_restau = FormRestaurant(instance = e_restaurante)
		else:
			var_restau=FormRestaurant(request.POST, instance = e_restaurante)
			if var_restau.is_valid():
				var_restau.save()
			return redirect('index')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'crud/lugares/form_restaurante.html', {'var_restau': var_restau, 'error': error})


def EliminarColegio(request, cod_colegio):
	var_cole = colegio.objects.get(cod_colegio=cod_colegio)
	var_cole.delete()
	return redirect('crud:list_colegio')


def EliminarIglesia(request, cod_iglesia):
	var_iglesia = iglesia.objects.get(cod_iglesia=cod_iglesia)
	var_iglesia.delete()
	return redirect('crud:list_iglesia')


def EliminarPlaza(request, cod_plaza):
	var_plaza = plaza.objects.get(cod_plaza=cod_plaza)
	var_plaza.delete()
	return redirect('crud:list_plaza')


def EliminarRestaurante(request, cod_restaurante):
	var_restau = restaurante.objects.get(cod_restaurante=cod_restaurante)
	var_restau.delete()
	return redirect('crud:list_restaurante')

def EliminarAlojamiento(request, cod_alojamiento):
	var_alojamiento = alojamiento.objects.get(cod_alojamiento=cod_alojamiento)
	var_alojamiento.delete()
	return redirect('crud:list_alojamiento')



def AñadirEvento(request):
	if request.method =='POST':
		var_evento= FormEvento(request.POST)
		if var_evento.is_valid():
			var_evento.save()
			return redirect('index')
	else:
		var_evento = FormEvento()
	return render(request,'crud/calendario/form_evento.html',{'var_evento': var_evento})


def AgregarFoto(request):
	if request.method =='POST':
		var_foto= FormFoto(request.POST, request.FILES)
		if var_foto.is_valid():
			var_foto.save()
			return redirect('index')
	else:
		var_foto = FormFoto()
	return render(request,'crud/calendario/form_foto.html',{'var_foto': var_foto})


def ListarEvento(request):
	e_lista = evento.objects.all() 
	return render(request,'crud/calendario/listar_evento.html',{'e_lista': e_lista})

def ListarFoto(request):
	f_lista = foto.objects.all() 
	return render(request,'crud/calendario/listar_foto.html',{'f_lista': f_lista})

def EditarEvento(request, cod_evento):
	var_evento= None
	error = None
	try:
		e_evento = evento.objects.get(cod_evento=cod_evento)
		if request.method == 'GET':
			var_evento = FormEvento(instance = e_evento)
		else:
			var_evento= FormEvento(request.POST, instance = e_evento)
			if var_evento.is_valid():
				var_evento.save()
			return redirect('index')
	except ObjectDoesNotExist as e:
		error = e
	return render(request, 'crud/calendario/form_evento.html',{'var_evento': var_evento, 'error': error})

def EditarFoto(request, cod_foto):
	var_foto= None
	error = None
	try:
		e_foto = foto.objects.get(cod_foto=cod_foto)
		if request.method == 'GET':
			var_foto = FormFoto(instance = e_foto)
		else:
			var_foto= FormFoto(request.POST, request.Files, instance = e_foto)
			if var_foto.is_valid():
				var_foto.save()
			return redirect('index')
	except ObjectDoesNotExist as e:
		error = e
	return render(request, 'crud/calendario/form_foto.html',{'var_foto': var_foto, 'error': error})

def EliminarEvento(request, cod_evento):
	var_evento = evento.objects.get(cod_evento=cod_evento)
	var_evento.delete()
	return redirect('crud:list_evento')

def EliminarFoto(request, cod_foto):
	var_foto = foto.objects.get(cod_foto=cod_foto)
	var_foto.delete()
	return redirect('crud:list_foto')

def MostrarMapa(request):
	m_lista=admin_agregar.objects.all()
	p_lista=plaza.objects.all()
	i_lista=iglesia.objects.all()
	r_lista=restaurante.objects.all()
	c_lista=colegio.objects.all()
	a_lista=alojamiento.objects.all()
	return render(request,'mapa_main/mapa.html',{'m_lista':m_lista,'p_lista':p_lista,'i_lista':i_lista,'r_lista':r_lista,'c_lista':c_lista,'a_lista':a_lista})