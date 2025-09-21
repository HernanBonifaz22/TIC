import tkinter as tk
from tkinter import ttk, messagebox
import datetime


class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        # Lista para almacenar eventos
        self.eventos = []

        # Configurar estilo
        self.setup_estilos()

        # Crear interfaz
        self.crear_interfaz()

    def setup_estilos(self):
        """Configura estilos para la aplicación"""
        style = ttk.Style()
        style.theme_use('clam')

        # Configurar colores
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10), padding=5)
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Treeview', rowheight=25)
        style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))

    def crear_interfaz(self):
        """Crea todos los componentes de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Título
        titulo = ttk.Label(main_frame, text="Agenda Personal", style='Header.TLabel')
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Frame para entrada de datos
        input_frame = ttk.LabelFrame(main_frame, text="Nuevo Evento", padding="10")
        input_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N), padx=(0, 10))
        input_frame.columnconfigure(1, weight=1)

        # Etiquetas y campos de entrada
        ttk.Label(input_frame, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.fecha_entry = ttk.Entry(input_frame, width=15)
        self.fecha_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(5, 0))
        self.fecha_entry.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))

        ttk.Label(input_frame, text="Hora (HH:MM):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.hora_entry = ttk.Entry(input_frame, width=15)
        self.hora_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(5, 0))
        self.hora_entry.insert(0, "12:00")

        ttk.Label(input_frame, text="Descripción:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.desc_entry = ttk.Entry(input_frame, width=30)
        self.desc_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(5, 0))

        # Botones
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Eliminar Evento", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Salir", command=self.root.quit).pack(side=tk.LEFT, padx=5)

        # Frame para la lista de eventos
        list_frame = ttk.LabelFrame(main_frame, text="Eventos Programados", padding="10")
        list_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Treeview para mostrar eventos
        columns = ('fecha', 'hora', 'descripcion')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings')

        # Definir columnas
        self.tree.heading('fecha', text='Fecha')
        self.tree.heading('hora', text='Hora')
        self.tree.heading('descripcion', text='Descripción')

        self.tree.column('fecha', width=100, anchor=tk.CENTER)
        self.tree.column('hora', width=80, anchor=tk.CENTER)
        self.tree.column('descripcion', width=200, anchor=tk.W)

        # Scrollbar para el treeview
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Configurar pesos para la expansión
        list_frame.rowconfigure(0, weight=1)
        list_frame.columnconfigure(0, weight=1)

    def validar_fecha(self, fecha_str):
        """Valida que el formato de fecha sea correcto (YYYY-MM-DD)"""
        try:
            datetime.datetime.strptime(fecha_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validar_hora(self, hora_str):
        """Valida que el formato de hora sea correcto (HH:MM)"""
        try:
            datetime.datetime.strptime(hora_str, '%H:%M')
            return True
        except ValueError:
            return False

    def agregar_evento(self):
        """Agrega un nuevo evento a la lista"""
        fecha = self.fecha_entry.get().strip()
        hora = self.hora_entry.get().strip()
        descripcion = self.desc_entry.get().strip()

        # Validaciones
        if not fecha:
            messagebox.showerror("Error", "Por favor, ingrese una fecha.")
            return

        if not self.validar_fecha(fecha):
            messagebox.showerror("Error", "Formato de fecha incorrecto. Use YYYY-MM-DD (ej. 2024-09-21).")
            return

        if not hora:
            messagebox.showerror("Error", "Por favor, ingrese una hora.")
            return

        if not self.validar_hora(hora):
            messagebox.showerror("Error", "Formato de hora incorrecto. Use HH:MM (ej. 14:30).")
            return

        if not descripcion:
            messagebox.showerror("Error", "Por favor, ingrese una descripción.")
            return

        # Agregar a la lista de eventos
        self.eventos.append({
            'fecha': fecha,
            'hora': hora,
            'descripcion': descripcion
        })

        # Agregar al treeview
        self.tree.insert('', tk.END, values=(fecha, hora, descripcion))

        # Limpiar campos (excepto fecha)
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.hora_entry.insert(0, "12:00")

        messagebox.showinfo("Éxito", "Evento agregado correctamente.")

    def eliminar_evento(self):
        """Elimina el evento seleccionado"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")
            return

        # Pedir confirmación
        respuesta = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de que desea eliminar el evento seleccionado?"
        )

        if respuesta:
            # Obtener valores del item seleccionado
            item_values = self.tree.item(selected_item[0], 'values')

            # Eliminar de la lista de eventos
            for evento in self.eventos:
                if (evento['fecha'] == item_values[0] and
                        evento['hora'] == item_values[1] and
                        evento['descripcion'] == item_values[2]):
                    self.eventos.remove(evento)
                    break

            # Eliminar del treeview
            self.tree.delete(selected_item[0])

            messagebox.showinfo("Éxito", "Evento eliminado correctamente.")


def main():
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()


if __name__ == "__main__":
    main()