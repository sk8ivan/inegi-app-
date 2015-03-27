from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView,CreateView
from .forms import Windows, Parches, Prueba
from .models import Equipo,Parche, Equipo

# Create your views here.
class Inicio(TemplateView):
	template_name = 'inicio.html'

class Exito(TemplateView):
	template_name = 'exito.html'

class Configuracion(TemplateView):
	template_name = 'menu.html'

class Equipos(ListView):
	template_name = 'equipos.html'
	model = Equipo

class listaParches(ListView):
	template_name = 'listaParches.html'
	model = Parche



def AltaWindows(request):
	
	if request.method == 'POST':
		form = Windows(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/exito.html/')
	

	else:
		form = Windows()

	return render(request, 'windows.html', {'form':form})

def AltaParche(request):

	if request.method == 'POST':
		form = Parches(request.POST)
		
		if form.is_valid():
			print ("Hola soy valido")
			form.save()
			
			return HttpResponseRedirect('/listaParches/')

	else:
		form = Parches()

	return render(request, 'formularios/parches.html', {'form':form})


def AltaEquipo(request):
	path = r'C:\\Users\\soporte.drcs\\Documents\\GitHub\\inegi\\inegi\\media\\archivos'
	if request.method == 'POST':
		form = Prueba(request.POST)

		if form.is_valid():
			form.save()
			equipos = Equipo.objects.all()
			#escribiendo en el archivo
			outfile = open(path + 'equipos.txt', 'w')
			for x in range(len(equipos)):
				outfile.write(str(equipos[x]) + ",")
			
			outfile.close()
			print(equipos)
			return HttpResponseRedirect('/equipos/')
	

	else:
		form = Prueba()

	return render(request, 'formularios/AltaEquipos.html', {'form':form})
















