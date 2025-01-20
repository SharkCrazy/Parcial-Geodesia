import math
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np  # Importar numpy

a = 6378137  # Radio ecuatorial en metros (aproximado para el elipsoide WGS-84)
b = 6356752.314245  # Radio polar en metros (aproximado para el elipsoide WGS-84)

# Función para la proyección directa de Mercator
def proyeccion_mercator_directa(lon, lat, lon0):
    lon_rad = math.radians(lon)
    lat_rad = math.radians(lat)
    lon0_rad = math.radians(lon0)
    
    x = a * (lon_rad - lon0_rad)
    y = a * math.log(math.tan(math.pi / 4 + lat_rad / 2))
    
    return x, y

# Función para la proyección inversa de Mercator
def proyeccion_mercator_inversa(x, y, lon0):
    lon0_rad = math.radians(lon0)
    
    lon_rad = x / a + lon0_rad
    lat_rad = 2 * math.atan(math.exp(y / a)) - math.pi / 2
    
    lon = math.degrees(lon_rad)
    lat = math.degrees(lat_rad)
    
    return lon, lat

# Función para graficar el elipsoide, el punto y su proyección en el mapa
def plot_elipsoideYProyeccion(lon, lat, lon0):
    fig = plt.figure(figsize=(12, 6))
    
    # Crear el elipsoide en 3D
    ax1 = fig.add_subplot(121, projection='3d')
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = a * np.outer(np.cos(u), np.sin(v))
    y = a * np.outer(np.sin(u), np.sin(v))
    z = b * np.outer(np.ones(np.size(u)), np.cos(v))
    
    ax1.plot_surface(x, y, z, color='b', alpha=0.6)
    
    # Graficar el punto en el elipsoide
    lon_rad = math.radians(lon)
    lat_rad = math.radians(lat)
    x_point = a * math.cos(lat_rad) * math.cos(lon_rad)
    y_point = a * math.cos(lat_rad) * math.sin(lon_rad)
    z_point = b * math.sin(lat_rad)
    ax1.scatter(x_point, y_point, z_point, color='r', s=100, label='Punto Original')
    
    ax1.set_title('Elipsoide 3D')
    ax1.legend()
    
    # Crear el mapa con la proyección de Mercator
    ax2 = fig.add_subplot(122, projection=ccrs.Mercator())
    
    # Añadir características del mapa
    ax2.add_feature(cfeature.COASTLINE)
    ax2.add_feature(cfeature.BORDERS, linestyle=':')
    ax2.add_feature(cfeature.LAND, edgecolor='black')
    ax2.add_feature(cfeature.OCEAN)
    ax2.add_feature(cfeature.LAKES, edgecolor='black')
    ax2.add_feature(cfeature.RIVERS)
    
    # Definir los límites del área de Colombia
    ax2.set_extent([-79, -66, -4, 12], crs=ccrs.PlateCarree())
    
    # Graficar el punto original
    ax2.plot(lon, lat, 'ro', markersize=5, transform=ccrs.PlateCarree(), label='Punto Original')
    
    # Calcular la proyección
    x_proj, y_proj = proyeccion_mercator_directa(lon, lat, lon0)
    lon_proj, lat_proj = proyeccion_mercator_inversa(x_proj, y_proj, lon0)
    
    # Graficar el punto proyectado
    ax2.plot(lon_proj, lat_proj, 'bo', markersize=5, transform=ccrs.PlateCarree(), label='Punto Proyectado')
    
    ax2.set_title('Proyección de Mercator')
    ax2.legend()
    
    plt.show()

# Función para manejar la proyección directa
def handle_direct_projection():
    try:
        lon = float(entry_lon.get())
        lat = float(entry_lat.get())
        lon0 = float(entry_lon0.get())
        x, y = proyeccion_mercator_directa(lon, lat, lon0)
        messagebox.showinfo("Proyección Directa", f"x = {x}, y = {y}")
        plot_elipsoideYProyeccion(lon, lat, lon0)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

# Función para manejar la proyección inversa
def handle_inverse_projection():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        lon0 = float(entry_lon0.get())
        lon, lat = proyeccion_mercator_inversa(x, y, lon0)
        messagebox.showinfo("Proyección Inversa", f"longitud = {lon}, latitud = {lat}")
        plot_elipsoideYProyeccion(lon, lat, lon0)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Proyección de Mercator")

# Crear y colocar los widgets
tk.Label(root, text="Longitud (grados):").grid(row=0, column=0)
entry_lon = tk.Entry(root)
entry_lon.grid(row=0, column=1)

tk.Label(root, text="Latitud (grados):").grid(row=1, column=0)
entry_lat = tk.Entry(root)
entry_lat.grid(row=1, column=1)

tk.Label(root, text="Longitud central del mapa (grados):").grid(row=2, column=0)
entry_lon0 = tk.Entry(root)
entry_lon0.grid(row=2, column=1)

tk.Label(root, text="Latitud de origen (grados):").grid(row=3, column=0)
entry_lat0 = tk.Entry(root)
entry_lat0.grid(row=3, column=1)

tk.Button(root, text="Proyección Directa", command=handle_direct_projection).grid(row=4, column=0, columnspan=2)

tk.Label(root, text="Coordenada x:").grid(row=5, column=0)
entry_x = tk.Entry(root)
entry_x.grid(row=5, column=1)

tk.Label(root, text="Coordenada y:").grid(row=6, column=0)
entry_y = tk.Entry(root)
entry_y.grid(row=6, column=1)

tk.Button(root, text="Proyección Inversa", command=handle_inverse_projection).grid(row=7, column=0, columnspan=2)

# Añadir un botón para mostrar el mapa
tk.Button(root, text="Mostrar Mapa", command=plot_elipsoideYProyeccion).grid(row=8, column=0, columnspan=2)

# Verificación de la integridad del programa
if __name__ == "__main__":
    # Coordenadas de prueba
    lon = -74.06527778  # Longitud de Bogotá
    lat = 4.628055556   # Latitud de Bogotá
    lon0 = 0         # Longitud central del mapa (Meridiano de Greenwich)

    # Proyección directa
    x, y = proyeccion_mercator_directa(lon, lat, lon0)
    print(f"Proyección Directa: x = {x}, y = {y}")

    # Proyección inversa
    lon_inv, lat_inv = proyeccion_mercator_inversa(x, y, lon0)
    print(f"Proyección Inversa: longitud = {lon_inv}, latitud = {lat_inv}")

    # Verificación
    print(f"Coordenadas originales: longitud = {lon}, latitud = {lat}")
    print(f"Coordenadas proyectadas inversamente: longitud = {lon_inv}, latitud = {lat_inv}")

# Iniciar el bucle principal de la interfaz
root.mainloop()