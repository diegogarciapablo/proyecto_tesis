from django.shortcuts import render, redirect
from .form_lugar import formlugar

def paso1(request):
	return render(request,'crud/choice_add.html')

def añadirlugar(request):
	if request.method == 'POST':
		flugar=formlugar(request.POST)
		if flugar.is_valid():
			flugar.save()
			return redirect('index')
	else:
		flugar=formlugar()
	return render(request,'crud/lugares/add_lugar.html', {'flugar': flugar})