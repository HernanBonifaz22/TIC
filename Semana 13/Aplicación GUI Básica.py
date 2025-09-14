import tkinter as tk
from tkinter import messagebox


class AplicacionTareas:
    def __init__(self, root):
        # Configurar la ventana principal
        self.root = root
        self.root.title("Mi Lista de Tareas")
        self.root.geometry("400x400")

        # Lista para almacenar las tareas
        self.tareas = []

        # Crear y colocar los componentes en la ventana
        self.crear_widgets()

    def crear_widgets(self):
        # Etiqueta de instrucción
        self.lbl_instruccion = tk.Label(
            self.root,
            text="Ingrese una tarea:",
            font=("Arial", 12)
        )
        self.lbl_instruccion.pack(pady=10)

        # Campo de texto para ingresar tareas
        self.entrada_tarea = tk.Entry(
            self.root,
            width=40,
            font=("Arial", 10)
        )
        self.entrada_tarea.pack(pady=5)
        self.entrada_tarea.bind("<Return>", lambda event: self.agregar_tarea())  # Enter para agregar

        # Marco para los botones
        self.marco_botones = tk.Frame(self.root)
        self.marco_botones.pack(pady=10)

        # Botón Agregar
        self.btn_agregar = tk.Button(
            self.marco_botones,
            text="Agregar",
            command=self.agregar_tarea,
            bg="lightgreen",
            width=10
        )
        self.btn_agregar.pack(side=tk.LEFT, padx=5)

        # Botón Limpiar
        self.btn_limpiar = tk.Button(
            self.marco_botones,
            text="Limpiar",
            command=self.limpiar_tareas,
            bg="lightcoral",
            width=10
        )
        self.btn_limpiar.pack(side=tk.LEFT, padx=5)

        # Etiqueta para la lista
        self.lbl_lista = tk.Label(
            self.root,
            text="Tareas:",
            font=("Arial", 12, "bold")
        )
        self.lbl_lista.pack(pady=(20, 5))

        # Listbox para mostrar las tareas
        self.lista_tareas = tk.Listbox(
            self.root,
            width=50,
            height=12,
            font=("Arial", 10)
        )
        self.lista_tareas.pack(pady=5, padx=10)

        # Botón para eliminar tarea seleccionada
        self.btn_eliminar = tk.Button(
            self.root,
            text="Eliminar Seleccionada",
            command=self.eliminar_tarea,
            bg="lightyellow"
        )
        self.btn_eliminar.pack(pady=5)

    def agregar_tarea(self):
        # Obtener texto del campo de entrada
        tarea = self.entrada_tarea.get().strip()

        # Validar que no esté vacío
        if tarea:
            # Agregar a la lista y al listbox
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, f"{len(self.tareas)}. {tarea}")

            # Limpiar el campo de entrada
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def limpiar_tareas(self):
        # Preguntar confirmación antes de limpiar
        respuesta = messagebox.askyesno(
            "Confirmar",
            "¿Está seguro de que desea eliminar todas las tareas?"
        )

        if respuesta:
            # Limpiar la lista y el listbox
            self.tareas.clear()
            self.lista_tareas.delete(0, tk.END)

    def eliminar_tarea(self):
        # Obtener índice seleccionado
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            indice = seleccion[0]

            # Eliminar de la lista y del listbox
            self.tareas.pop(indice)
            self.lista_tareas.delete(indice)

            # Renumerar las tareas restantes
            self.renumerar_tareas()
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")

    def renumerar_tareas(self):
        # Limpiar y volver a agregar todas las tareas con nueva numeración
        self.lista_tareas.delete(0, tk.END)
        for i, tarea in enumerate(self.tareas, 1):
            self.lista_tareas.insert(tk.END, f"{i}. {tarea}")


# Función principal para ejecutar la aplicación
def main():
    root = tk.Tk()
    app = AplicacionTareas(root)
    root.mainloop()


if __name__ == "__main__":
    main()