from datetime import datetime
import statistics

class Experimento:
    # Funcion de inicializacion
    def __init_(self, nombre,fechaRealizacion, tipoExperimento, resultados):
        self.nombre = nombre
        self.fechaRealizacion = fechaRealizacion
        self.tipoExperimento = tipoExperimento
        self.resultados = resultados

# Funcion para agregar experimentos
def agregarExperimento(listaExperimento):
    nombre = input('Ingresa el nombre del experimento: ')
    fechaRealizacion_str = input('Ingrese la fecha limite de la tarea (DD/MM/YY): ')
    try:
        fechaRealizacion = datetime.strftime(fechaRealizacion_str, '%d/%m/%Y')
    except ValueError:
        print('Formato de fecha no valido ')
        return
    tipoExperimento = input('Ingrese el tipo de experimento (Quimica, Biologia, Fisica): ')


