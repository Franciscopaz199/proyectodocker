from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ControlTareas.Models.tarea import Tarea
from django.urls import reverse
from django.contrib import messages


class LibPrograma:

    def Agregar(self, request):

        if self.verificar(request):
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            fecha = request.POST.get('fecha')
            tarea1 = Tarea(Tarea.getId(),nombre, descripcion, fecha)
            tarea1.save()
            messages.success(request, 'Se ha agregado la tarea correctamente')
            return redirect('admin')
        return HttpResponseRedirect(reverse('/'))

    def listar(self, request):
        if self.verificar(request):
            tareas = Tarea.obtenerTareas()
            return render(request, "listar.html",{'tareas':tareas} )
        return HttpResponseRedirect(reverse('/'))
    
    def eliminar(self,request):
        if self.verificar(request):
            tareas = Tarea.obtenerTareas()
            return render(request,"eliminar.html",{'tareas':tareas})
        return HttpResponseRedirect(reverse('/'))
        
    def eliminartarea(self,request):
        if self.verificar(request):
            id = request.POST.get('id')
            Tarea.eliminarTarea(id)

            messages.success(request, "Tarea eliminada con exito")

            if int(request.POST["atrasada"]) == 1:
                return redirect("atrasadas")
            
            return redirect("eliminar")
        return HttpResponseRedirect(reverse('/'))
    
    
    def actualizar(self,request):
        if self.verificar(request):
            id = request.POST.get('id')
            tarea = Tarea.obtenerTarea(id)
            return render(request,"actualizar.html",{'tarea':tarea})
        return HttpResponseRedirect(reverse('/'))

    def actualizartarea(self,request):
        if self.verificar(request):
            id = request.POST.get('id')
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            fecha = request.POST.get('fecha')
            Tarea.actualizarTarea(id,nombre,descripcion,fecha)
            messages.success(request, "Se ha actualizado la tarea")
            return redirect('actualizar')
        return HttpResponseRedirect(reverse('/'))

    def fecha(self, request):
        if self.verificar(request):
            if request.method == 'POST':
                fecha = request.POST.get('fecha')
                tareas = Tarea.obtenerTareasFecha(fecha)
                if len(tareas) == 0:
                    messages.error(request, 'No hay tareas para mostrar')
                return render(request, "fechas2.html",{'fechas':tareas, 'fecha':fecha} )
            else:
                return render(request, "fecha.html")
        return HttpResponseRedirect(reverse('/'))

    def contar(self, request):
        if self.verificar(request):
            tareas = Tarea.obtenerTareas()
            tamano = len(tareas)
            return render(request, "contar.html",{'tamano':tamano} )
        return HttpResponseRedirect(reverse('/'))

    def atrasadas(self, request):
        if self.verificar(request):
            tareas = Tarea.obtenerTareasAtrasadas()
            return render(request, "atrasadas.html",{'tareas':tareas} )
        return HttpResponseRedirect(reverse('/'))


    def tareasMes(self, request):
        if self.verificar(request):
            tareas = Tarea.tareasMes()
            return render(request, "tareames.html",{'tareas':tareas} )
        return HttpResponseRedirect(reverse('/'))
    

    def verificar(self,request):
        my_cookie = request.COOKIES.get('my_cookie')
        if my_cookie == 'my_value':
            return True
        return False