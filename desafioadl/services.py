from desafioadl.models import *

def listar_tareas_y_subtareas():
    tareas = Tarea.objects.filter(eliminada=False) 
    for tarea in tareas:
        subtareas = tarea.subtarea_set.filter(eliminada=False) 
        print(f"Tarea: {tarea.descripcion}")
        for subtarea in subtareas:
            print(f"  Subtarea: {subtarea.descripcion}")
    return list(tareas)

def crear_nueva_tarea(descripcion):
    nueva_tarea = Tarea.objects.create(descripcion=descripcion)
    return listar_tareas_y_subtareas()

def crear_subtarea(descripcion, tarea_id):    
    nueva_subtarea = SubTarea.objects.create(descripcion=descripcion, tarea_id=tarea_id)
    return listar_tareas_y_subtareas()

def borrar_subtarea(subtarea_id):   
    subtarea = SubTarea.objects.get(pk=subtarea_id) 
    subtarea.eliminada = True
    subtarea.save()
    return listar_tareas_y_subtareas()

def borrar_tarea(tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id) 
    tarea.eliminada = True 
    tarea.save()
    return listar_tareas_y_subtareas()

def mostrar(tareas):
    for i, tarea in enumerate(tareas, start=1):
        print(f"[{i}] {tarea.descripcion}")
        for j, subtarea in enumerate(tarea.subtarea_set.filter(eliminada=False), start=1):
            print(f".... [{i}.{j}] {subtarea.descripcion}")