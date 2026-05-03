from django.shortcuts import render, redirect
from db_peewee import Tarea # Importamos tu modelo de Peewee

def lista_tareas(request):
    if request.method == 'POST':
        # Agregar tarea con Peewee
        nueva = Tarea(nombre=request.POST.get('tarea'), descripcion="")
        nueva.save()
        return redirect('/')

    # Leer tareas con Peewee
    tareas = Tarea.select()
    return render(request, 'index.html', {'tareas': tareas})

def eliminar_tarea(request, id):
    # Eliminar tarea con Peewee
    try:
        tarea = Tarea.get(Tarea.id == id)
        tarea.delete_instance()
    except Tarea.DoesNotExist:
        pass
    return redirect('/')