# Distancia de Hausdorff para Shapefiles de Áreas de Endemismo

Este proyecto contiene scripts de Python para calcular la matriz de distancias de Hausdorff entre un conjunto de archivos shapefile de polígonos (Áreas de Endemismo). La distancia de Hausdorff mide cuán lejos están dos geometrías entre sí.

El script procesa todos los shapefiles de un directorio, calcula la distancia por pares y guarda los resultados en un archivo CSV.

## Características

- Carga automática de todos los archivos `.shp` de un directorio.
- Unificación de geometrías por capa para un cálculo eficiente.
- Cálculo de la matriz de distancias de Hausdorff.
- Exportación de la matriz de resultados a un archivo CSV.
- **Versión alternativa (`main1.py`)** con barras de progreso para una mejor experiencia de usuario en procesos largos.

## Scripts Disponibles

- **`main.py`**: La versión base y funcional del script.
- **`main1.py`**: Una versión que utiliza la librería `tqdm` para mostrar barras de progreso durante la carga de datos, el procesamiento y el guardado de resultados. Se recomienda usar este script para conjuntos de datos grandes.

## Datos

- **`datos/`**: Esta carpeta contiene los datos originales con los que se obtuvieron los resultados para el artículo.
- **`datos_ejemplo/`**: Esta carpeta contiene un pequeño conjunto de datos para propósitos demostrativos.

## Requisitos

- Python 3.8 o superior
- Las librerías listadas en `requirements.txt`.

## Uso

1.  **Prepara tus datos**: Coloca tus archivos shapefile (`.shp` y sus archivos asociados `.dbf`, `.shx`, etc.) en la carpeta `datos_ejemplo`, o crea una nueva carpeta y actualiza la variable `directory` en el script.

2.  **Configura el script (Opcional)**:
    Si deseas usar una carpeta de datos diferente o cambiar el nombre del archivo de salida, puedes modificar las siguientes líneas al principio del script (`main.py` o `main1.py`):
    ```python
    # Ruta del directorio donde se encuentran los shapefiles
    directory = 'datos_ejemplo' # Cambia a 'datos' o tu carpeta personalizada

    # Ruta y nombre del archivo CSV donde se guardarán los resultados.
    output_file = 'dist_ex.csv' # Puedes cambiar el nombre del archivo de salida
    ```

3.  **Ejecuta el script**

4.  **Revisa los resultados**: Una vez finalizado el proceso, encontrarás el archivo CSV (por defecto, `dist_ex.csv`) en el directorio principal. 
