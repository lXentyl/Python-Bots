import os
import csv
import tkinter as tk
from tkinter import messagebox, filedialog

# Función para crear carpetas basadas en el cuatrimestre y el horario del CSV
def crear_carpetas():
    cuatrimestre = cuatrimestre_entry.get()
    ruta_base = ruta_entry.get()
    horario_path = horario_entry.get()
    
    if not ruta_base or not cuatrimestre or not horario_path:
        messagebox.showwarning("Advertencia", "Por favor, ingresa la ruta, cuatrimestre y archivo CSV.")
        return
    
    # Crear carpeta del cuatrimestre
    ruta_cuatrimestre = os.path.join(ruta_base, cuatrimestre)
    
    if not os.path.exists(ruta_cuatrimestre):
        os.makedirs(ruta_cuatrimestre)

    # Leer el horario del archivo CSV
    try:
        with open(horario_path, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltar la cabecera
            
            # Crear carpetas para las materias
            for fila in lector:
                dia = fila[0]
                materias = fila[1:]  # Tomar todas las materias en la fila
                
                for materia in materias:
                    materia = materia.strip()  # Eliminar espacios en blanco
                    if materia:  # Evitar carpetas vacías
                        ruta_carpeta = os.path.join(ruta_cuatrimestre, materia)
                        if not os.path.exists(ruta_carpeta):
                            os.makedirs(ruta_carpeta)
        
        messagebox.showinfo("Éxito", f"Carpetas creadas correctamente en el cuatrimestre {cuatrimestre}.")
    
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo CSV no se encuentra. Verifica la ruta.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Creador de Carpetas Universitarias")
root.geometry("400x500")
root.config(bg="#2C3E50")

# Estilo y colores llamativos
titulo_label = tk.Label(root, text="Creador de Carpetas", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
titulo_label.pack(pady=20)

# Campo para ingresar la ruta base
ruta_label = tk.Label(root, text="Ruta base:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
ruta_label.pack(pady=5)

ruta_entry = tk.Entry(root, width=30)
ruta_entry.pack(pady=5)

# Campo para ingresar el cuatrimestre
cuatrimestre_label = tk.Label(root, text="Cuatrimestre:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
cuatrimestre_label.pack(pady=5)

cuatrimestre_entry = tk.Entry(root, width=30)
cuatrimestre_entry.pack(pady=5)

# Campo para ingresar la ruta del archivo CSV
horario_label = tk.Label(root, text="Archivo CSV del horario:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
horario_label.pack(pady=5)

horario_entry = tk.Entry(root, width=30)
horario_entry.pack(pady=5)

# Botón para seleccionar el archivo CSV
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo CSV", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    horario_entry.delete(0, tk.END)  # Limpiar el campo
    horario_entry.insert(0, archivo)  # Insertar la ruta del archivo seleccionado

seleccionar_btn = tk.Button(root, text="Seleccionar Archivo CSV", command=seleccionar_archivo, bg="#E74C3C", fg="#ECF0F1")
seleccionar_btn.pack(pady=10)

# Botón para crear carpetas
crear_btn = tk.Button(root, text="Crear Carpetas", font=("Helvetica", 12, "bold"), bg="#E74C3C", fg="#ECF0F1", command=crear_carpetas)
crear_btn.pack(pady=20)

root.mainloop()
