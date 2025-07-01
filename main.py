# 1. Importación de librerías
import os
import geopandas as gpd
import csv

# 2. Configuración de rutas
# Establece el directorio de trabajo actual.
os.chdir('D:\\Biogeoconserv\\endemshp')

# Ruta del directorio donde se encuentran los shapefiles
directory = 'datos_ejemplo'

# Ruta y nombre del archivo CSV donde se guardarán los resultados.
output_file = 'dist_ex.csv'

# 3. Carga de datos geoespaciales
# Obtiene una lista con los nombres (sin extensión) de todos los archivos que terminan en .shp en el directorio especificado.
shapefiles = [os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith('.shp')]

# Carga cada shapefile en un GeoDataFrame de GeoPandas y lo almacena en una lista.
layers = []
for shapefile in [f"{s}.shp" for s in shapefiles]:
    layer = gpd.read_file(os.path.join(directory, shapefile))
    layer = layer.to_crs(layer.crs)
    layers.append(layer)

# 4. Preparación para el cálculo
# Obtiene el número total de capas cargadas.
n = len(layers)
# Crea una matriz cuadrada de N x N, inicializada con ceros, para almacenar las distancias.
distances = [[0.0 for _ in range(n)] for _ in range(n)]

# Se unifican las geometrías de cada capa una sola vez antes de los cálculos.
print("Unificando geometrías de cada capa...")
unified_geometries = [layer.geometry.unary_union for layer in layers]

# 5. Cálculo de la matriz de distancias
print("Calculando la matriz de distancias de Hausdorff...")
# Bucle anidado para calcular la distancia de Hausdorff entre cada par de geometrías.
# El bucle interno `range(a + 1, n)` asegura que cada par se compare una sola vez,
# para evitar cálculos redundantes y comparaciones de una capa consigo misma.
for a in range(n):
    for b in range(a + 1, n):
        # Calcula la distancia de Hausdorff entre la geometría 'a' y la 'b'.
        dist = unified_geometries[a].hausdorff_distance(unified_geometries[b])
        # Asigna el resultado a la matriz en ambas posiciones simétricas.
        distances[a][b] = dist
        distances[b][a] = dist

# 6. Guardado de resultados
# Abrir archivo de salida en modo escritura.
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Escribe la primera fila (encabezados) con los nombres de los shapefiles.
    writer.writerow([''] + shapefiles)
    # Itera sobre la matriz de distancias para escribir cada fila en el archivo CSV.
    for a, row in enumerate(distances):
        # Escribe el nombre del shapefile de la fila seguido de todos los valores de distancia.
        writer.writerow([shapefiles[a]] + row)

# Imprime un mensaje para indicar que el proceso ha finalizado.
print(f"Los resultados se han guardado en el archivo '{output_file}'")
