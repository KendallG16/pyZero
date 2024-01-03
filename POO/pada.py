import tkinter as tk
from tkinter import simpledialog

class Persona:
    def __init__(self, nombre: str, edad: int, estatura: float) -> None:
        self.nombre = nombre 
        self.edad = edad
        self.estatura = estatura

def mostrarFormularioCrear():
    limpiarFormulario()
    label_opcion.config(text="Creando Persona")
    label_nombre.grid(row=1, column=0, padx=5, pady=5)
    entry_nombre.grid(row=1, column=1, padx=5, pady=5)
    label_edad.grid(row=2, column=0, padx=5, pady=5)
    entry_edad.grid(row=2, column=1, padx=5, pady=5)
    label_estatura.grid(row=3, column=0, padx=5, pady=5)
    entry_estatura.grid(row=3, column=1, padx=5, pady=5)
    boton_guardar.config(text="Guardar", command=crearPersona)

def mostrarFormularioBorrar():
    limpiarFormulario()
    label_opcion.config(text="Borrando Persona")
    label_nombre.grid(row=1, column=0, padx=5, pady=5)
    entry_nombre.grid(row=1, column=1, padx=5, pady=5)
    boton_guardar.config(text="Borrar", command=borrarPersona)

def mostrarFormularioModificar():
    limpiarFormulario()
    label_opcion.config(text="Modificando Datos")
    label_nombre.grid(row=1, column=0, padx=5, pady=5)
    entry_nombre.grid(row=1, column=1, padx=5, pady=5)
    boton_guardar.config(text="Modificar", command=modificarDatos)

def limpiarFormulario():
    label_opcion.config(text="")
    label_nombre.grid_remove()
    label_edad.grid_remove()
    label_estatura.grid_remove()
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    entry_nombre.grid_remove()
    entry_edad.grid_remove()
    entry_estatura.grid_remove()

def crearPersona():
    nombre = entry_nombre.get()
    edad = int(entry_edad.get())
    estatura = float(entry_estatura.get())
    nueva_persona = Persona(nombre, edad, estatura)
    personas.append(nueva_persona)
    mostrarPersonas()
    limpiarFormulario()

def borrarPersona():
    personaEliminar = entry_nombre.get()
    for i in range(len(personas)):
        if personas[i].nombre == personaEliminar:
            del personas[i]
            break
    mostrarPersonas()
    limpiarFormulario()

def mostrarPersonas():
    texto_personas.delete(1.0, tk.END)
    for i, persona in enumerate(personas, 1):
        texto_personas.insert(tk.END, f"{i}. Nombre: {persona.nombre}, Edad: {persona.edad}, Estatura: {persona.estatura}\n")

def modificarDatos():
    personaModificar = entry_nombre.get()
    for i in range(len(personas)):
        if personas[i].nombre == personaModificar:
            opcion = simpledialog.askinteger("Modificar Datos", "Edad: 1\nEstatura: 2\nIngrese la opción a modificar:")
            if opcion == 1:
                nueva_edad = int(simpledialog.askstring("Modificar Datos", "Ingrese la nueva edad:"))
                personas[i].edad = nueva_edad
            elif opcion == 2:
                nueva_estatura = float(simpledialog.askstring("Modificar Datos", "Ingrese la nueva estatura:"))
                personas[i].estatura = nueva_estatura
    mostrarPersonas()
    limpiarFormulario()

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Personas")

# Frame para el formulario
frame_formulario = tk.Frame(root)
frame_formulario.pack()

label_opcion = tk.Label(frame_formulario, text="", font=("Arial", 12, "bold"))
label_opcion.grid(row=0, columnspan=2)

label_nombre = tk.Label(frame_formulario, text="Nombre:")
entry_nombre = tk.Entry(frame_formulario)
label_edad = tk.Label(frame_formulario, text="Edad:")
entry_edad = tk.Entry(frame_formulario)
label_estatura = tk.Label(frame_formulario, text="Estatura:")
entry_estatura = tk.Entry(frame_formulario)
boton_guardar = tk.Button(frame_formulario, text="", command=None)

# Botones para operaciones
topbar = tk.Frame(root)
topbar.pack(side=tk.TOP, fill=tk.X)

boton_crear = tk.Button(topbar, text="Crear Persona", command=mostrarFormularioCrear)
boton_crear.pack(side=tk.LEFT, padx=5, pady=5)

boton_borrar = tk.Button(topbar, text="Borrar Persona", command=mostrarFormularioBorrar)
boton_borrar.pack(side=tk.LEFT, padx=5, pady=5)

boton_modificar = tk.Button(topbar, text="Modificar Datos", command=mostrarFormularioModificar)
boton_modificar.pack(side=tk.LEFT, padx=5, pady=5)

# Texto para mostrar las personas
texto_personas = tk.Text(root)
texto_personas.pack()

# Lista de personas
personas = []

root.mainloop()

