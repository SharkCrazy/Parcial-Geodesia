# main.py
import tkinter as tk
from tkinter import messagebox
from parametros import a, b, f, e2, e22
from calculos import longitud_arco_meridiano, sexagesimal_a_decimal, longitud_arco_paralelo, longitud_arco_paralelo_con_longitudes, calcular_area_cuadrilátero

def actualizar_parametros():
    global a, b, f, e2, e22
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        f = (a - b) / a
        e2 = ((a**2) - (b**2)) / (a**2)
        e22 = e2 / (1 - e2)
        messagebox.showinfo("Parámetros Actualizados", "Los parámetros del elipsoide se han actualizado correctamente.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores válidos para los parámetros.")

def calcular_meridiano():
    try:
        # Latitud 1
        lat1_grados = int(entry_lat1_grados.get())
        lat1_minutos = int(entry_lat1_minutos.get())
        lat1_segundos = float(entry_lat1_segundos.get())  # Permitir segundos en decimales
        lat1_decimal = sexagesimal_a_decimal(lat1_grados, lat1_minutos, lat1_segundos)
        
        # Latitud 2
        lat2_grados = int(entry_lat2_grados.get())
        lat2_minutos = int(entry_lat2_minutos.get())
        lat2_segundos = float(entry_lat2_segundos.get())  # Permitir segundos en decimales
        lat2_decimal = sexagesimal_a_decimal(lat2_grados, lat2_minutos, lat2_segundos)
        
        resultado = longitud_arco_meridiano(lat1_decimal, lat2_decimal)
        messagebox.showinfo("Resultado Meridiano", f"La longitud del arco del meridiano entre {lat1_grados}°{lat1_minutos}'{lat1_segundos}\" y {lat2_grados}°{lat2_minutos}'{lat2_segundos}\" es de {resultado:.6f} metros.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores válidos.")

def calcular_paralelo():
    try:
        # Latitud
        lat_grados = int(entry_lat_grados.get())
        lat_minutos = int(entry_lat_minutos.get())
        lat_segundos = float(entry_lat_segundos.get())  # Permitir segundos en decimales
        lat_decimal = sexagesimal_a_decimal(lat_grados, lat_minutos, lat_segundos)
        
        if option.get() == 1:
            # Ángulo entre las longitudes
            delta_long_grados = int(entry_delta_long_grados.get())
            delta_long_minutos = int(entry_delta_long_minutos.get())
            delta_long_segundos = float(entry_delta_long_segundos.get())  # Permitir segundos en decimales
            delta_long_decimal = sexagesimal_a_decimal(delta_long_grados, delta_long_minutos, delta_long_segundos)
            
            resultado = longitud_arco_paralelo(lat_decimal, delta_long_decimal)
            messagebox.showinfo("Resultado Paralelo", f"La longitud del arco del paralelo a {lat_grados}°{lat_minutos}'{lat_segundos}\" con un ángulo de {delta_long_grados}°{delta_long_minutos}'{delta_long_segundos}\" es de {resultado:.6f} metros.")
        else:
            # Longitud 1
            lon1_grados = int(entry_lon1_grados.get())
            lon1_minutos = int(entry_lon1_minutos.get())
            lon1_segundos = float(entry_lon1_segundos.get())  # Permitir segundos en decimales
            lon1_decimal = sexagesimal_a_decimal(lon1_grados, lon1_minutos, lon1_segundos)
            
            # Longitud 2
            lon2_grados = int(entry_lon2_grados.get())
            lon2_minutos = int(entry_lon2_minutos.get())
            lon2_segundos = float(entry_lon2_segundos.get())  # Permitir segundos en decimales
            lon2_decimal = sexagesimal_a_decimal(lon2_grados, lon2_minutos, lon2_segundos)
            
            resultado = longitud_arco_paralelo_con_longitudes(lat_decimal, lon1_decimal, lon2_decimal)
            messagebox.showinfo("Resultado Paralelo", f"La longitud del arco del paralelo a {lat_grados}°{lat_minutos}'{lat_segundos}\" entre las longitudes {lon1_grados}°{lon1_minutos}'{lon1_segundos}\" y {lon2_grados}°{lon2_minutos}'{lon2_segundos}\" es de {resultado:.6f} metros.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores válidos.")

def calcular_area_cuadrilátero_gui():
    try:
        # Latitud 1
        lat1_grados = int(entry_lat1_grados.get())
        lat1_minutos = int(entry_lat1_minutos.get())
        lat1_segundos = float(entry_lat1_segundos.get())
        lat1_decimal = sexagesimal_a_decimal(lat1_grados, lat1_minutos, lat1_segundos)
        if var_lat1.get() == "S":
            lat1_decimal = -lat1_decimal
        
        # Latitud 2
        lat2_grados = int(entry_lat2_grados.get())
        lat2_minutos = int(entry_lat2_minutos.get())
        lat2_segundos = float(entry_lat2_segundos.get())
        lat2_decimal = sexagesimal_a_decimal(lat2_grados, lat2_minutos, lat2_segundos)
        if var_lat2.get() == "S":
            lat2_decimal = -lat2_decimal
        
        # Longitud 1
        lon1_grados = int(entry_lon1_grados.get())
        lon1_minutos = int(entry_lon1_minutos.get())
        lon1_segundos = float(entry_lon1_segundos.get())
        lon1_decimal = sexagesimal_a_decimal(lon1_grados, lon1_minutos, lon1_segundos)
        if var_lon1.get() == "W":
            lon1_decimal = -lon1_decimal
        
        # Longitud 2
        lon2_grados = int(entry_lon2_grados.get())
        lon2_minutos = int(entry_lon2_minutos.get())
        lon2_segundos = float(entry_lon2_segundos.get())
        lon2_decimal = sexagesimal_a_decimal(lon2_grados, lon2_minutos, lon2_segundos)
        if var_lon2.get() == "W":
            lon2_decimal = -lon2_decimal
        
        # Calcular área
        area = calcular_area_cuadrilátero(lat1_decimal, lon1_decimal, lat2_decimal, lon2_decimal)
        messagebox.showinfo("Resultado Área", f"El área del cuadrilátero es de {area:.6-+f} metros cuadrados.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores válidos.")

def mostrar_entradas():
    if option.get() == 1:
        frame_delta_long.grid(row=2, column=0, columnspan=4, pady=10)
        frame_longitudes.grid_forget()
    else:
        frame_longitudes.grid(row=2, column=0, columnspan=4, pady=10)
        frame_delta_long.grid_forget()

# Crear la ventana principal
root = tk.Tk()
root.title("Algoritmo 1")

# Crear frame para actualizar los parámetros del elipsoide
frame_parametros = tk.Frame(root)
frame_parametros.pack(pady=10)

label_a = tk.Label(frame_parametros, text="a:")
label_a.grid(row=0, column=0, padx=5)
entry_a = tk.Entry(frame_parametros, width=15)
entry_a.grid(row=0, column=1, padx=5)
entry_a.insert(0, str(a))

label_b = tk.Label(frame_parametros, text="b:")
label_b.grid(row=1, column=0, padx=5)
entry_b = tk.Entry(frame_parametros, width=15)
entry_b.grid(row=1, column=1, padx=5)
entry_b.insert(0, str(b))

button_actualizar_parametros = tk.Button(frame_parametros, text="Actualizar Parámetros", command=actualizar_parametros)
button_actualizar_parametros.grid(row=2, column=0, columnspan=2, pady=10)

# Crear frame para las opciones de entrada de paralelo
frame_opciones = tk.Frame(root)
frame_opciones.pack(pady=10)

option = tk.IntVar()
option.set(1)  # Opción por defecto

radio_delta_long = tk.Radiobutton(frame_opciones, text="Usar ángulo entre longitudes", variable=option, value=1, command=mostrar_entradas)
radio_delta_long.grid(row=0, column=0, padx=10)

radio_longitudes = tk.Radiobutton(frame_opciones, text="Usar dos longitudes", variable=option, value=2, command=mostrar_entradas)
radio_longitudes.grid(row=0, column=1, padx=10)

# Crear frame para las entradas de paralelo
frame_entradas_paralelo = tk.Frame(root)
frame_entradas_paralelo.pack(pady=10)

# Latitud
label_lat = tk.Label(frame_entradas_paralelo, text="Latitud (grados, minutos, segundos):")
label_lat.grid(row=0, column=0, padx=5)
entry_lat_grados = tk.Entry(frame_entradas_paralelo, width=5)
entry_lat_grados.grid(row=0, column=1, padx=5)
entry_lat_minutos = tk.Entry(frame_entradas_paralelo, width=5)
entry_lat_minutos.grid(row=0, column=2, padx=5)
entry_lat_segundos = tk.Entry(frame_entradas_paralelo, width=10)
entry_lat_segundos.grid(row=0, column=3, padx=5)

# Frame para ángulo entre longitudes
frame_delta_long = tk.Frame(frame_entradas_paralelo)

label_delta_long = tk.Label(frame_delta_long, text="Ángulo entre longitudes (grados, minutos, segundos):")
label_delta_long.grid(row=0, column=0, padx=5)
entry_delta_long_grados = tk.Entry(frame_delta_long, width=5)
entry_delta_long_grados.grid(row=0, column=1, padx=5)
entry_delta_long_minutos = tk.Entry(frame_delta_long, width=5)
entry_delta_long_minutos.grid(row=0, column=2, padx=5)
entry_delta_long_segundos = tk.Entry(frame_delta_long, width=10)
entry_delta_long_segundos.grid(row=0, column=3, padx=5)

# Frame para dos longitudes
frame_longitudes = tk.Frame(frame_entradas_paralelo)

# Longitud 1
label_lon1 = tk.Label(frame_longitudes, text="Longitud 1 (grados, minutos, segundos):")
label_lon1.grid(row=0, column=0, padx=5)
entry_lon1_grados = tk.Entry(frame_longitudes, width=5)
entry_lon1_grados.grid(row=0, column=1, padx=5)
entry_lon1_minutos = tk.Entry(frame_longitudes, width=5)
entry_lon1_minutos.grid(row=0, column=2, padx=5)
entry_lon1_segundos = tk.Entry(frame_longitudes, width=10)
entry_lon1_segundos.grid(row=0, column=3, padx=5)

# Longitud 2
label_lon2 = tk.Label(frame_longitudes, text="Longitud 2 (grados, minutos, segundos):")
label_lon2.grid(row=1, column=0, padx=5)
entry_lon2_grados = tk.Entry(frame_longitudes, width=5)
entry_lon2_grados.grid(row=1, column=1, padx=5)
entry_lon2_minutos = tk.Entry(frame_longitudes, width=5)
entry_lon2_minutos.grid(row=1, column=2, padx=5)
entry_lon2_segundos = tk.Entry(frame_longitudes, width=10)
entry_lon2_segundos.grid(row=1, column=3, padx=5)

# Botón para calcular paralelo
button_calcular_paralelo = tk.Button(root, text="Calcular Paralelo", command=calcular_paralelo)
button_calcular_paralelo.pack(pady=10)

# Crear frame para las entradas de meridiano
frame_entradas_meridiano = tk.Frame(root)
frame_entradas_meridiano.pack(pady=10)

# Latitud 1
label_lat1 = tk.Label(frame_entradas_meridiano, text="Latitud 1 (grados, minutos, segundos):")
label_lat1.grid(row=0, column=0, padx=5)
entry_lat1_grados = tk.Entry(frame_entradas_meridiano, width=5)
entry_lat1_grados.grid(row=0, column=1, padx=5)
entry_lat1_minutos = tk.Entry(frame_entradas_meridiano, width=5)
entry_lat1_minutos.grid(row=0, column=2, padx=5)
entry_lat1_segundos = tk.Entry(frame_entradas_meridiano, width=10)
entry_lat1_segundos.grid(row=0, column=3, padx=5)

# Latitud 2
label_lat2 = tk.Label(frame_entradas_meridiano, text="Latitud 2 (grados, minutos, segundos):")
label_lat2.grid(row=1, column=0, padx=5)
entry_lat2_grados = tk.Entry(frame_entradas_meridiano, width=5)
entry_lat2_grados.grid(row=1, column=1, padx=5)
entry_lat2_minutos = tk.Entry(frame_entradas_meridiano, width=5)
entry_lat2_minutos.grid(row=1, column=2, padx=5)
entry_lat2_segundos = tk.Entry(frame_entradas_meridiano, width=10)
entry_lat2_segundos.grid(row=1, column=3, padx=5)

# Botón para calcular meridiano
button_calcular_meridiano = tk.Button(root, text="Calcular Meridiano", command=calcular_meridiano)
button_calcular_meridiano.pack(pady=10)

label_a = tk.Label(frame_parametros, text="a:")
label_a.grid(row=0, column=0, padx=5)
entry_a = tk.Entry(frame_parametros, width=15)
entry_a.grid(row=0, column=1, padx=5)
entry_a.insert(0, str(a))

label_b = tk.Label(frame_parametros, text="b:")
label_b.grid(row=1, column=0, padx=5)
entry_b = tk.Entry(frame_parametros, width=15)
entry_b.grid(row=1, column=1, padx=5)
entry_b.insert(0, str(b))

button_actualizar_parametros = tk.Button(frame_parametros, text="Actualizar Parámetros", command=actualizar_parametros)
button_actualizar_parametros.grid(row=2, column=0, columnspan=2, pady=10)

def calcular_area_cuadrilátero_gui():
    try:
        # Latitud 1
        lat1_grados = int(entry_lat1_grados.get())
        lat1_minutos = int(entry_lat1_minutos.get())
        lat1_segundos = float(entry_lat1_segundos.get())
        lat1_decimal = sexagesimal_a_decimal(lat1_grados, lat1_minutos, lat1_segundos)
        if var_lat1.get() == "S":
            lat1_decimal = -lat1_decimal
        
        # Latitud 2
        lat2_grados = int(entry_lat2_grados.get())
        lat2_minutos = int(entry_lat2_minutos.get())
        lat2_segundos = float(entry_lat2_segundos.get())
        lat2_decimal = sexagesimal_a_decimal(lat2_grados, lat2_minutos, lat2_segundos)
        if var_lat2.get() == "S":
            lat2_decimal = -lat2_decimal
        
        # Longitud 1
        lon1_grados = int(entry_lon1_grados.get())
        lon1_minutos = int(entry_lon1_minutos.get())
        lon1_segundos = float(entry_lon1_segundos.get())
        lon1_decimal = sexagesimal_a_decimal(lon1_grados, lon1_minutos, lon1_segundos)
        if var_lon1.get() == "W":
            lon1_decimal = -lon1_decimal
        
        # Longitud 2
        lon2_grados = int(entry_lon2_grados.get())
        lon2_minutos = int(entry_lon2_minutos.get())
        lon2_segundos = float(entry_lon2_segundos.get())
        lon2_decimal = sexagesimal_a_decimal(lon2_grados, lon2_minutos, lon2_segundos)
        if var_lon2.get() == "W":
            lon2_decimal = -lon2_decimal
        
        # Calcular área
        area = calcular_area_cuadrilátero(lat1_decimal, lon1_decimal, lat2_decimal, lon2_decimal)
        messagebox.showinfo("Resultado Área", f"El área del cuadrilátero es de {area:.6f} metros cuadrados.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores válidos.")


# Crear frame para las entradas de los vértices del cuadrilátero
frame_entradas = tk.Frame(root)
frame_entradas.pack(pady=10)

# Latitud 1
label_lat1 = tk.Label(frame_entradas, text="Latitud 1 (grados, minutos, segundos):")
label_lat1.grid(row=0, column=0, padx=5)
entry_lat1_grados = tk.Entry(frame_entradas, width=5)
entry_lat1_grados.grid(row=0, column=1, padx=5)
entry_lat1_minutos = tk.Entry(frame_entradas, width=5)
entry_lat1_minutos.grid(row=0, column=2, padx=5)
entry_lat1_segundos = tk.Entry(frame_entradas, width=10)
entry_lat1_segundos.grid(row=0, column=3, padx=5)

var_lat1 = tk.StringVar(value="N")
radio_lat1_n = tk.Radiobutton(frame_entradas, text="N", variable=var_lat1, value="N")
radio_lat1_s = tk.Radiobutton(frame_entradas, text="S", variable=var_lat1, value="S")
radio_lat1_n.grid(row=0, column=4)
radio_lat1_s.grid(row=0, column=5)

# Longitud 1
label_lon1 = tk.Label(frame_entradas, text="Longitud 1 (grados, minutos, segundos):")
label_lon1.grid(row=1, column=0, padx=5)
entry_lon1_grados = tk.Entry(frame_entradas, width=5)
entry_lon1_grados.grid(row=1, column=1, padx=5)
entry_lon1_minutos = tk.Entry(frame_entradas, width=5)
entry_lon1_minutos.grid(row=1, column=2, padx=5)
entry_lon1_segundos = tk.Entry(frame_entradas, width=10)
entry_lon1_segundos.grid(row=1, column=3, padx=5)

var_lon1 = tk.StringVar(value="E")
radio_lon1_e = tk.Radiobutton(frame_entradas, text="E", variable=var_lon1, value="E")
radio_lon1_w = tk.Radiobutton(frame_entradas, text="W", variable=var_lon1, value="W")
radio_lon1_e.grid(row=1, column=4)
radio_lon1_w.grid(row=1, column=5)

# Latitud 2
label_lat2 = tk.Label(frame_entradas, text="Latitud 2 (grados, minutos, segundos):")
label_lat2.grid(row=2, column=0, padx=5)
entry_lat2_grados = tk.Entry(frame_entradas, width=5)
entry_lat2_grados.grid(row=2, column=1, padx=5)
entry_lat2_minutos = tk.Entry(frame_entradas, width=5)
entry_lat2_minutos.grid(row=2, column=2, padx=5)
entry_lat2_segundos = tk.Entry(frame_entradas, width=10)
entry_lat2_segundos.grid(row=2, column=3, padx=5)

var_lat2 = tk.StringVar(value="N")
radio_lat2_n = tk.Radiobutton(frame_entradas, text="N", variable=var_lat2, value="N")
radio_lat2_s = tk.Radiobutton(frame_entradas, text="S", variable=var_lat2, value="S")
radio_lat2_n.grid(row=2, column=4)
radio_lat2_s.grid(row=2, column=5)

# Longitud 2
label_lon2 = tk.Label(frame_entradas, text="Longitud 2 (grados, minutos, segundos):")
label_lon2.grid(row=3, column=0, padx=5)
entry_lon2_grados = tk.Entry(frame_entradas, width=5)
entry_lon2_grados.grid(row=3, column=1, padx=5)
entry_lon2_minutos = tk.Entry(frame_entradas, width=5)
entry_lon2_minutos.grid(row=3, column=2, padx=5)
entry_lon2_segundos = tk.Entry(frame_entradas, width=10)
entry_lon2_segundos.grid(row=3, column=3, padx=5)

var_lon2 = tk.StringVar(value="E")
radio_lon2_e = tk.Radiobutton(frame_entradas, text="E", variable=var_lon2, value="E")
radio_lon2_w = tk.Radiobutton(frame_entradas, text="W", variable=var_lon2, value="W")
radio_lon2_e.grid(row=3, column=4)
radio_lon2_w.grid(row=3, column=5)

# Botón para calcular el área del cuadrilátero
button_calcular_area = tk.Button(root, text="Calcular Área del Cuadrilátero", command=calcular_area_cuadrilátero_gui)
button_calcular_area.pack(pady=10)
# Ejecutar el bucle principal de la interfaz
root.mainloop()
