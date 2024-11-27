# Sistema de Gestión de Experimentos

Este proyecto es un sistema interactivo para gestionar, analizar y generar informes de experimentos científicos. Está desarrollado en Python y permite registrar experimentos, visualizar datos, realizar análisis estadístico y generar un informe final en formato de texto.

## Características

- **Registro de Experimentos**: Añade experimentos indicando nombre, fecha, tipo y resultados.
- **Visualización de Datos**: Muestra los detalles de todos los experimentos registrados.
- **Análisis Estadístico**: Calcula el promedio, el valor máximo y mínimo de los resultados de cada experimento.
- **Generación de Informes**: Crea un archivo de texto con un informe detallado de todos los experimentos.

## Estructura del Código
**Experimento:** Clase que modela un experimento con atributos como nombre, fecha, tipo y resultados.

### Funciones principales:

- **agregar_experimento**: Permite agregar nuevos experimentos.
- **visualizar_experimentos**: Muestra todos los experimentos registrados.
- **analisis_resultados**: Realiza análisis estadístico de los resultados.
- **generar_informe**: Genera un informe final en un archivo de texto.


**Menú principal:**

--- Menú Principal ---
1. Agregar experimento
2. Visualizar experimentos
3. Analizar resultados
4. Generar informe
5. Salir
Seleccione una opción:

### Informe Generado:

- **Nombre**: Experimento 1
- **Fecha de realización**: 25/11/2024
- **Tipo de experimento**: Química
- **Resultados**: 
  - 12.3
  - 15.4
  - 10.0
- **Estadísticas**:
  - **Promedio**: 12.57
  - **Máximo**: 15.4
  - **Mínimo**: 10.0

