# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Proyect
from .forms import ProyectForm

# Vista para la lista de proyectos
def proyect_list(request):
    proyects = Proyect.objects.all()
    
    # Si la solicitud es en formato JSON
    if request.GET.get('format') == 'json':
        # Creamos un diccionario con los datos de los proyectos
        proyect_data = [{"nombre": proyect.nombre, "rut": proyect.rut, "correo": proyect.correo} for proyect in proyects]
        
        # Retornamos los datos en formato JSON
        return JsonResponse(proyect_data, safe=False)
    
    # Si no es JSON, mostramos la página con la lista de proyectos
    return render(request, 'proyect_list.html', {'proyects': proyects})

# Vista para crear un proyecto
def proyect_create(request):
    if request.method == 'POST':
        form = ProyectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyect_list')
    else:
        form = ProyectForm()
    return render(request, 'proyect_form.html', {'form': form})

# Vista para ver los detalles de un proyecto
def proyect_detail(request, pk):
    proyect = get_object_or_404(Proyect, pk=pk)
    return render(request, 'proyect_detail.html', {'proyect': proyect})

# Vista para actualizar un proyecto
def proyect_update(request, pk):
    proyect = get_object_or_404(Proyect, pk=pk)
    if request.method == 'POST':
        form = ProyectForm(request.POST, instance=proyect)
        if form.is_valid():
            form.save()
            return redirect('proyect_list')
    else:
        form = ProyectForm(instance=proyect)
    return render(request, 'proyect_form.html', {'form': form})

# Vista para eliminar un proyecto
def proyect_delete(request, pk):
    proyect = get_object_or_404(Proyect, pk=pk)
    if request.method == 'POST':
        proyect.delete()
        return redirect('proyect_list')
    return render(request, 'proyect_confirm_delete.html', {'proyect': proyect})
