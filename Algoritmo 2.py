import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt

class NivelacionGeodesica:
    def __init__(self, root):
        self.root = root
        self.root.title("Nivelación Geodésica")
        self.estaciones = []  # Lista para almacenar las estaciones, cotas y alturas instrumentales
        self.vistas_intermedias = []  # Lista para almacenar vistas intermedias

        # Crear la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y campos de entrada
        tk.Label(self.root, text="Nombre del punto:").grid(row=0, column=0)
        self.estacion_entry = tk.Entry(self.root)
        self.estacion_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Cota:").grid(row=1, column=0)
        self.cota_entry = tk.Entry(self.root)
        self.cota_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Vista más:").grid(row=2, column=0)
        self.vista_mas_entry = tk.Entry(self.root)
        self.vista_mas_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Vista menos:").grid(row=3, column=0)
        self.vista_menos_entry = tk.Entry(self.root)
        self.vista_menos_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Distancia:").grid(row=4, column=0)
        self.distancia_entry = tk.Entry(self.root)
        self.distancia_entry.grid(row=4, column=1)

        # Botón para agregar punto inicial
        tk.Button(self.root, text="Agregar Punto", command=self.agregar_punto).grid(row=5, column=0, columnspan=2)

        # Botón para agregar vista intermedia
        tk.Button(self.root, text="Agregar Vista Intermedia", command=self.agregar_vista_intermedia).grid(row=6, column=0, columnspan=2)

        # Botón para mostrar gráfica
        tk.Button(self.root, text="Mostrar Gráfica", command=self.mostrar_grafica).grid(row=7, column=0, columnspan=2)

        # Tabla para mostrar resultados
        self.tree = ttk.Treeview(self.root, columns=("Estación", "Cota", "Vista Más", "Vista Menos", "Sube", "Baja", "Cota Instrumental", "Distancia"), show='headings')
        self.tree.heading("Estación", text="Estación")
        self.tree.heading("Cota", text="Cota")
        self.tree.heading("Vista Más", text="Vista Más")
        self.tree.heading("Vista Menos", text="Vista Menos")
        self.tree.heading("Sube", text="Sube")
        self.tree.heading("Baja", text="Baja")
        self.tree.heading("Cota Instrumental", text="Cota Instrumental")
        self.tree.heading("Distancia", text="Distancia")
        self.tree.grid(row=8, column=0, columnspan=2)

    def agregar_punto(self):
        estacion = self.estacion_entry.get()
        vista_mas = self.vista_mas_entry.get()
        vista_menos = self.vista_menos_entry.get()
        distancia = self.distancia_entry.get()

        if not estacion or not vista_mas or not vista_menos or not distancia:
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        vista_mas = float(vista_mas)
        vista_menos = float(vista_menos)
        distancia = float(distancia)
        
        if self.estaciones:
            cota_anterior = self.estaciones[-1]['cota']
            cota_instrumental_anterior = self.estaciones[-1]['cota_instrumental']
            cota_nueva = cota_instrumental_anterior - vista_menos
            cota_instrumental = cota_nueva + vista_mas
            delta = cota_nueva - cota_anterior
            if delta > 0:
                sube = delta
                baja = 0
            else:
                sube = 0
                baja = abs(delta)
        else:
            cota_anterior = float(self.cota_entry.get())
            cota_nueva = cota_anterior
            cota_instrumental = cota_nueva + vista_mas
            sube = vista_mas
            baja = 0
        
        self.estaciones.append({'estacion': estacion, 'cota': cota_nueva, 'vista_mas': vista_mas, 'vista_menos': vista_menos, 'sube': sube, 'baja': baja, 'cota_instrumental': cota_instrumental, 'distancia': distancia})
        self.tree.insert("", "end", values=(estacion, cota_nueva, vista_mas, vista_menos, sube, baja, cota_instrumental, distancia))
        messagebox.showinfo("Información", f"Estación {estacion} registrada con cota = {cota_nueva:.6f}, sube = {sube:.6f}, baja = {baja:.6f}, altura instrumental = {cota_instrumental:.6f} y distancia = {distancia:.2f}.")
        self.limpiar_campos()

    def agregar_vista_intermedia(self):
        estacion_intermedia = self.estacion_entry.get()
        vista_menos = self.vista_menos_entry.get()
        distancia = self.distancia_entry.get()

        if not estacion_intermedia or not vista_menos or not distancia:
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        vista_menos = float(vista_menos)
        distancia = float(distancia)
        cota_instrumental = self.estaciones[-1]['cota_instrumental']
        cota_intermedia = cota_instrumental - vista_menos
        cota_anterior = self.estaciones[-1]['cota']
        delta = cota_intermedia - cota_anterior
        if delta > 0:
            sube = delta
            baja = 0
        else:
            sube = 0
            baja = abs(delta)
        self.vistas_intermedias.append({'estacion': estacion_intermedia, 'vista_menos': vista_menos, 'cota': cota_intermedia, 'sube': sube, 'baja': baja, 'distancia': distancia})
        self.tree.insert("", "end", values=(estacion_intermedia, cota_intermedia, "", vista_menos, sube, baja, "", distancia))
        messagebox.showinfo("Información", f"Vista intermedia {estacion_intermedia} registrada con cota = {cota_intermedia:.6f}, sube = {sube:.6f}, baja = {baja:.6f} y distancia = {distancia:.2f}.")
        self.limpiar_campos()

    def mostrar_grafica(self):
        distancias = [0]
        cotas = [self.estaciones[0]['cota']]

        for estacion in self.estaciones[1:]:
            distancias.append(distancias[-1] + estacion['distancia'])
            cotas.append(estacion['cota'])

        for vista in self.vistas_intermedias:
            distancias.append(distancias[-1] + vista['distancia'])
            cotas.append(vista['cota'])

        plt.plot(distancias, cotas, marker='o')
        plt.xlabel('Distancia')
        plt.ylabel('Cota')
        plt.title('Nivelación Geodésica')
        plt.grid(True)
        plt.show()

    def limpiar_campos(self):
        self.estacion_entry.delete(0, tk.END)
        self.cota_entry.delete(0, tk.END)
        self.vista_mas_entry.delete(0, tk.END)
        self.vista_menos_entry.delete(0, tk.END)
        self.distancia_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = NivelacionGeodesica(root)
    root.mainloop()