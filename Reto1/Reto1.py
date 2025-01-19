from datetime import datetime
import statistics

class Experimento:
    # Inicialización del objeto Experimento
    def __init__(self, nombre, fecha_realizacion, tipo_experimento, resultados):
        self.nombre = nombre
        self.fecha_realizacion = fecha_realizacion
        self.tipo_experimento = tipo_experimento
        self.resultados = resultados

# Función para agregar experimentos
def agregar_experimento(lista_experimentos):
    nombre = input('Ingresa el nombre del experimento: ')
    fecha_realizacion_str = input('Ingrese la fecha de realización (DD/MM/AAAA): ')
    try:
        fecha_realizacion = datetime.strptime(fecha_realizacion_str, '%d/%m/%Y')
    except ValueError:
        print('Formato de fecha no válido. Intente nuevamente.')
        return

    tipo_experimento = input('Ingrese el tipo de experimento (quimica, biologia, fisica): ').lower()
    if tipo_experimento not in ['quimica', 'biologia', 'fisica']:
        print('Tipo de experimento no reconocido. Intente nuevamente.')
        return

    resultados_str = input('Ingrese los resultados obtenidos (separados por comas): ')
    try:
        resultados = list(map(float, resultados_str.split(',')))
    except ValueError:
        print('Resultados inválidos. Asegúrese de ingresar números separados por comas.')
        return

    # Crear el experimento y agregarlo a la lista
    experimento = Experimento(nombre, fecha_realizacion, tipo_experimento, resultados)
    lista_experimentos.append(experimento)
    print('Experimento agregado con éxito.')

# Función para visualizar los experimentos
def visualizar_experimentos(lista_experimentos):
    if not lista_experimentos:
        print('No se encuentran experimentos creados.')
        return
    for i, experimento in enumerate(lista_experimentos, start=1):
        print(f'\nExperimento {i}')
        print(f'Nombre: {experimento.nombre}')
        print(f'Fecha de realización: {experimento.fecha_realizacion.strftime("%d/%m/%Y")}')
        print(f'Tipo de experimento: {experimento.tipo_experimento}')
        print(f'Resultados: {experimento.resultados}')

# Función para realizar análisis de resultados
def analisis_resultados(lista_experimentos):
    if not lista_experimentos:
        print('No se encuentran experimentos registrados.')
        return
    for experimento in lista_experimentos:
        promedio = statistics.mean(experimento.resultados)
        maximo = max(experimento.resultados)
        minimo = min(experimento.resultados)
        print(f'\nAnálisis del experimento: {experimento.nombre}')
        print(f'Promedio: {promedio:.2f}')
        print(f'Máximo: {maximo}')
        print(f'Mínimo: {minimo}')

# Función para generar un informe
def generar_informe(lista_experimentos):
    if not lista_experimentos:
        print('No hay experimentos registrados para generar un informe.')
        return
    informe = 'Informe Final de Experimentos\n\n'
    for experimento in lista_experimentos:
        promedio = statistics.mean(experimento.resultados)
        maximo = max(experimento.resultados)
        minimo = min(experimento.resultados)
        informe += (
            f'Nombre: {experimento.nombre}\n'
            f'Fecha de realización: {experimento.fecha_realizacion.strftime("%d/%m/%Y")}\n'
            f'Tipo de experimento: {experimento.tipo_experimento}\n'
            f'Resultados: {experimento.resultados}\n'
            f'Estadísticas:\n'
            f'\tPromedio: {promedio:.2f}\n'
            f'\tMáximo: {maximo}\n'
            f'\tMínimo: {minimo}\n\n'
        )
    with open('informe_experimentos.txt', 'w') as file:
        file.write(informe)
    print('Informe generado y guardado como "informe_experimentos.txt".')

# Menú principal
def menu():
    lista_experimentos = []
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar experimento")
        print("2. Visualizar experimentos")
        print("3. Analizar resultados")
        print("4. Generar informe")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_experimento(lista_experimentos)
        elif opcion == '2':
            visualizar_experimentos(lista_experimentos)
        elif opcion == '3':
            analisis_resultados(lista_experimentos)
        elif opcion == '4':
            generar_informe(lista_experimentos)
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()

