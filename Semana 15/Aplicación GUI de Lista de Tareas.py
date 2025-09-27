import tkinter as tk
from tkinter import ttk, messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x400")
        self.root.resizable(True, True)

        # Lista para almacenar las tareas (texto, completada)
        self.tasks = []

        self.setup_ui()

    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Campo de entrada para nuevas tareas
        ttk.Label(main_frame, text="Nueva Tarea:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))

        self.task_entry = ttk.Entry(main_frame, width=40)
        self.task_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=(0, 5))
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Botón Añadir Tarea
        self.add_button = ttk.Button(main_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=(5, 0), pady=(0, 5))

        # Frame para la lista de tareas
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Listbox para mostrar las tareas
        self.tasks_listbox = tk.Listbox(list_frame, height=15, selectmode=tk.SINGLE)
        self.tasks_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tasks_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.tasks_listbox.configure(yscrollcommand=scrollbar.set)

        # Bind doble clic para marcar como completada
        self.tasks_listbox.bind('<Double-Button-1>', lambda event: self.toggle_task_completion())

        # Frame para botones de acción
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)

        # Botón Marcar como Completada
        self.complete_button = ttk.Button(
            buttons_frame,
            text="Marcar como Completada",
            command=self.toggle_task_completion
        )
        self.complete_button.grid(row=0, column=0, padx=(0, 5))

        # Botón Eliminar Tarea
        self.delete_button = ttk.Button(
            buttons_frame,
            text="Eliminar Tarea",
            command=self.delete_task
        )
        self.delete_button.grid(row=0, column=1, padx=5)

        # Botón Limpiar Completadas
        self.clear_button = ttk.Button(
            buttons_frame,
            text="Limpiar Completadas",
            command=self.clear_completed_tasks
        )
        self.clear_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        """Añade una nueva tarea a la lista"""
        task_text = self.task_entry.get().strip()

        if task_text:
            # Añadir tarea a la lista interna
            self.tasks.append({"text": task_text, "completed": False})

            # Actualizar la lista visual
            self.update_tasks_display()

            # Limpiar el campo de entrada
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")

    def toggle_task_completion(self):
        """Marca/desmarca una tarea como completada"""
        selected_index = self.tasks_listbox.curselection()

        if selected_index:
            index = selected_index[0]
            # Cambiar estado de completado
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_tasks_display()

            # Mantener la selección
            self.tasks_listbox.selection_set(index)

    def delete_task(self):
        """Elimina la tarea seleccionada"""
        selected_index = self.tasks_listbox.curselection()

        if selected_index:
            index = selected_index[0]

            # Confirmar eliminación
            task_text = self.tasks[index]["text"]
            if messagebox.askyesno("Confirmar", f"¿Eliminar la tarea: '{task_text}'?"):
                # Eliminar tarea de la lista
                del self.tasks[index]
                self.update_tasks_display()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def clear_completed_tasks(self):
        """Elimina todas las tareas completadas"""
        # Filtrar solo las tareas no completadas
        self.tasks = [task for task in self.tasks if not task["completed"]]
        self.update_tasks_display()

    def update_tasks_display(self):
        """Actualiza la visualización de la lista de tareas"""
        # Limpiar la lista actual
        self.tasks_listbox.delete(0, tk.END)

        # Añadir cada tarea con formato según su estado
        for task in self.tasks:
            task_text = task["text"]
            if task["completed"]:
                # Tachar texto para tareas completadas
                task_text = f"✓ {task_text}"
                self.tasks_listbox.insert(tk.END, task_text)
                # Cambiar color de fondo para completadas
                self.tasks_listbox.itemconfig(tk.END, {'bg': '#d4edda', 'fg': '#155724'})
            else:
                self.tasks_listbox.insert(tk.END, f"○ {task_text}")


def main():
    # Crear ventana principal
    root = tk.Tk()

    # Crear la aplicación
    app = TodoApp(root)

    # Ejecutar el bucle principal
    root.mainloop()


if __name__ == "__main__":
    main()