import datetime


class Tarea:

    def __init__(self,id,nombre, descripcion, fecha):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha = fecha

    def delete(self):
        Tarea.eliminarTarea(self.id)


    def save(self):
        with open('ControlTareas/data/tareas.txt','a') as archivo:
            archivo.write(self.__str__() + '\n')


    def __str__(self):
        return  str(self.id) + "," +  self.nombre + "," + self.descripcion + ","  + self.fecha    


    @staticmethod
    def getId():
        with open('ControlTareas/data/tareas.txt','r') as archivo:
            id = 0
            for linea in archivo:
                id = linea.split(',')[0]
            return int(id) + 1

    @staticmethod
    def obtenerTareas():
        with open('ControlTareas/data/tareas.txt','r') as archivo:
            listaTareas = []
            for linea in archivo:
                linea = linea.strip("\n")
                listaTareas.append(Tarea(linea.split(',')[0],linea.split(',')[1], linea.split(',')[2], linea.split(',')[3]))
            return listaTareas
    
    
    @staticmethod
    def eliminarTarea(id):
        with open('ControlTareas/data/tareas.txt','r') as archivo:
            listaTareas = []
            for linea in archivo:
                if linea.split(',')[0] != id:
                    linea = linea.strip("\n")
                    listaTareas.append(Tarea(linea.split(',')[0],linea.split(',')[1], linea.split(',')[2], linea.split(',')[3]))
       
        with open('ControlTareas/data/tareas.txt','w') as archivo:
            for tarea in listaTareas:
                archivo.write(tarea.__str__() + '\n')


    @staticmethod
    def obtenerTarea(id):
        tareas = Tarea.obtenerTareas()
        for tarea in tareas:
            if tarea.id == id:
                return tarea
        return None

    @staticmethod
    def actualizarTarea(id, nombre, descripcion, fecha):
        with open('ControlTareas/data/tareas.txt','r') as archivo:
            listaTareas = []
            for linea in archivo:
                linea = linea.strip("\n")
                if linea.split(',')[0] == id:
                    listaTareas.append(Tarea(id,nombre, descripcion, fecha))
                else:
                    listaTareas.append(Tarea(linea.split(',')[0],linea.split(',')[1], linea.split(',')[2], linea.split(',')[3]))
       
        with open('ControlTareas/data/tareas.txt','w') as archivo:
            for tarea in listaTareas:
                archivo.write(tarea.__str__() + '\n')

    @staticmethod
    def obtenerTareasFecha(fechaa):
        tareas = Tarea.obtenerTareas()
        listaTareas = []
        for tarea in tareas:
            if tarea.fecha == fechaa:
                listaTareas.append(tarea)
        return listaTareas
    
    @staticmethod
    def obtenerTareasAtrasadas():
        tareas = Tarea.obtenerTareas()
        listaTareas = []
        for tarea in tareas:
            if datetime.datetime.strptime(tarea.fecha, '%Y-%m-%d') < datetime.datetime.today():
                listaTareas.append(tarea)
        return listaTareas

    @staticmethod
    def tareasMes():
        tareas = Tarea.obtenerTareas()
        listaTareas = []
        for tarea in tareas:
            if datetime.datetime.strptime(tarea.fecha, '%Y-%m-%d').month == datetime.datetime.today().month:
                listaTareas.append(tarea)
        return listaTareas