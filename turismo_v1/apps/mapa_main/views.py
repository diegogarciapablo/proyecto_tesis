from django.shortcuts import render

# Create your views here.
def Home (request):
	return render(request,'index.html')

def Mapa (request):
	return render(request,'mapa_main/mapa.html')

def Tour(request):
	return render(request,'virtual/recorrido.html')