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
    resultados = input('Ingrese los resultados ontenidos: ')

    #Se crea un objeto y se agrega a la lista de experimentos
    experimento = Experimento(nombre, fechaRealizacion, tipoExperimento, resultados)
    experimento.append(listaExperimento)


# Funcion para visualizar los experimentos
def visualizarExperimento(listaExperimento):
    if not listaExperimento:
        print('No se encuentran experimentos creados ')
        return
    for i, experimento in enumerate(listaExperimento, start=1):

        print(f'\nExperimento {i}')
        print(f'Nombre: {experimento.nombre}')
        print(f'Fecha de realización: {experimento.fechaRealizacionstrftime("%d/%m/%Y")}')
        print(f'Tipo de experimento: {experimento.tipoExperimento}')
        print(f'Resultados: {experimento.resultados}')

# Funcion para realizar analisis de los resultados
def analisisResultados(listaExperimentos):
    if not listaExperimentos:
        print('No se encuentran experimentos registrados ')
    for experimento in listaExperimentos:
        promedio = statistics.mean(experimento.resultados)
        maximo = max(experimento.resultados)
        minimo = min(experimento.resultados)
        print(f'\nAnalisis de experimento {experimento.nombre}')
        print(f'\nPromedio: {promedio}')
        print(f'\nMaximo: {maximo}')
        print(f'\nMinimi: {minimo}')

