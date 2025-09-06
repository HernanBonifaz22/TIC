class Libro:
    """
    Clase que representa un libro en la biblioteca digital.
    Utiliza tuplas para atributos inmutables como autor y título.
    """

    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        # Usamos tuplas para almacenar autor y título ya que son inmutables
        self._titulo = (titulo,)  # Tupla de un solo elemento
        self._autor = (autor,)  # Tupla de un solo elemento
        self.categoria = categoria
        self.isbn = isbn  # ISBN como identificador único

    @property
    def titulo(self):
        return self._titulo[0]

    @property
    def autor(self):
        return self._autor[0]

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} - {self.categoria} (ISBN: {self.isbn})"

    def __repr__(self):
        return f"Libro('{self.titulo}', '{self.autor}', '{self.categoria}', '{self.isbn}')"


class Usuario:
    """
    Clase que representa a un usuario de la biblioteca.
    Mantiene una lista de libros actualmente prestados.
    """

    def __init__(self, nombre: str, id_usuario: str):
        self.nombre = nombre
        self.id_usuario = id_usuario  # ID único del usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def prestar_libro(self, libro: Libro):
        """Añade un libro a la lista de libros prestados"""
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn: str):
        """Elimina un libro de la lista de libros prestados por ISBN"""
        for i, libro in enumerate(self.libros_prestados):
            if libro.isbn == isbn:
                return self.libros_prestados.pop(i)
        return None

    def listar_libros_prestados(self):
        """Devuelve la lista de libros prestados"""
        return self.libros_prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    """
    Clase principal que gestiona toda la biblioteca digital.
    Utiliza diccionarios para búsquedas eficientes y conjuntos para IDs únicos.
    """

    def __init__(self):
        # Diccionario para libros disponibles (ISBN -> Objeto Libro)
        self.libros_disponibles = {}
        # Conjunto para IDs de usuarios únicos
        self.ids_usuarios = set()
        # Diccionario para usuarios registrados (ID -> Objeto Usuario)
        self.usuarios_registrados = {}
        # Diccionario para historial de préstamos (ISBN -> ID Usuario)
        self.historial_prestamos = {}

    # Métodos para gestión de libros
    def añadir_libro(self, libro: Libro):
        """Añade un nuevo libro a la biblioteca"""
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
            return False
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro '{libro.titulo}' añadido correctamente.")
        return True

    def quitar_libro(self, isbn: str):
        """Elimina un libro de la biblioteca por ISBN"""
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro '{libro.titulo}' eliminado correctamente.")
            return True
        print(f"No se encontró ningún libro con ISBN {isbn}.")
        return False

    # Métodos para gestión de usuarios
    def registrar_usuario(self, nombre: str, id_usuario: str):
        """Registra un nuevo usuario en la biblioteca"""
        if id_usuario in self.ids_usuarios:
            print(f"El ID de usuario {id_usuario} ya está registrado.")
            return False

        nuevo_usuario = Usuario(nombre, id_usuario)
        self.usuarios_registrados[id_usuario] = nuevo_usuario
        self.ids_usuarios.add(id_usuario)
        print(f"Usuario '{nombre}' registrado correctamente con ID {id_usuario}.")
        return True

    def dar_de_baja_usuario(self, id_usuario: str):
        """Da de baja a un usuario de la biblioteca"""
        if id_usuario not in self.ids_usuarios:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")
            return False

        # Verificar que el usuario no tenga libros prestados
        usuario = self.usuarios_registrados[id_usuario]
        if usuario.libros_prestados:
            print(f"No se puede dar de baja al usuario {id_usuario} porque tiene libros prestados.")
            return False

        del self.usuarios_registrados[id_usuario]
        self.ids_usuarios.remove(id_usuario)
        print(f"Usuario {id_usuario} dado de baja correctamente.")
        return True

    # Métodos para préstamos y devoluciones
    def prestar_libro(self, isbn: str, id_usuario: str):
        """Presta un libro a un usuario"""
        # Verificar que el libro existe y está disponible
        if isbn not in self.libros_disponibles:
            print(f"No se encontró ningún libro con ISBN {isbn}.")
            return False

        # Verificar que el usuario existe
        if id_usuario not in self.ids_usuarios:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")
            return False

        # Obtener libro y usuario
        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios_registrados[id_usuario]

        # Prestar el libro
        usuario.prestar_libro(libro)
        self.historial_prestamos[isbn] = id_usuario

        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        return True

    def devolver_libro(self, isbn: str, id_usuario: str):
        """Devuelve un libro prestado por un usuario"""
        # Verificar que el usuario existe
        if id_usuario not in self.ids_usuarios:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")
            return False

        usuario = self.usuarios_registrados[id_usuario]
        libro_devuelto = usuario.devolver_libro(isbn)

        if libro_devuelto:
            if isbn in self.historial_prestamos:
                del self.historial_prestamos[isbn]
            print(f"Libro '{libro_devuelto.titulo}' devuelto por {usuario.nombre}.")
            return True
        else:
            print(f"El usuario {id_usuario} no tiene prestado el libro con ISBN {isbn}.")
            return False

    # Métodos de búsqueda
    def buscar_por_titulo(self, titulo: str):
        """Busca libros por título (búsqueda parcial)"""
        resultados = []
        for libro in self.libros_disponibles.values():
            if titulo.lower() in libro.titulo.lower():
                resultados.append(libro)
        return resultados

    def buscar_por_autor(self, autor: str):
        """Busca libros por autor (búsqueda parcial)"""
        resultados = []
        for libro in self.libros_disponibles.values():
            if autor.lower() in libro.autor.lower():
                resultados.append(libro)
        return resultados

    def buscar_por_categoria(self, categoria: str):
        """Busca libros por categoría (búsqueda exacta)"""
        resultados = []
        for libro in self.libros_disponibles.values():
            if libro.categoria.lower() == categoria.lower():
                resultados.append(libro)
        return resultados

    def buscar_por_isbn(self, isbn: str):
        """Busca un libro por ISBN (búsqueda exacta)"""
        return self.libros_disponibles.get(isbn, None)

    # Métodos de listado
    def listar_libros_prestados_usuario(self, id_usuario: str):
        """Lista todos los libros prestados a un usuario específico"""
        if id_usuario not in self.ids_usuarios:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")
            return []

        usuario = self.usuarios_registrados[id_usuario]
        return usuario.listar_libros_prestados()

    def listar_todos_libros(self):
        """Lista todos los libros disponibles en la biblioteca"""
        return list(self.libros_disponibles.values())

    def listar_todos_usuarios(self):
        """Lista todos los usuarios registrados"""
        return list(self.usuarios_registrados.values())

    def __str__(self):
        return (f"Biblioteca Digital - Libros: {len(self.libros_disponibles)}, "
                f"Usuarios: {len(self.usuarios_registrados)}, "
                f"Préstamos activos: {len(self.historial_prestamos)}")


# Función para probar el sistema
def probar_sistema():
    """Función de prueba para demostrar el funcionamiento del sistema"""
    print("=== INICIO DE PRUEBAS DEL SISTEMA DE BIBLIOTECA DIGITAL ===\n")

    # Crear instancia de biblioteca
    biblioteca = Biblioteca()

    # Añadir algunos libros
    print("1. Añadiendo libros a la biblioteca:")
    libros = [
        Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "978-8437604947"),
        Libro("1984", "George Orwell", "Ciencia ficción", "978-0451524935"),
        Libro("El Quijote", "Miguel de Cervantes", "Clásico", "978-8424113496"),
        Libro("Fahrenheit 451", "Ray Bradbury", "Ciencia ficción", "978-1451673319"),
        Libro("Crimen y castigo", "Fiódor Dostoyevski", "Clásico", "978-8420665156")
    ]

    for libro in libros:
        biblioteca.añadir_libro(libro)
    print()

    # Registrar usuarios
    print("2. Registrando usuarios:")
    biblioteca.registrar_usuario("Ana García", "USER001")
    biblioteca.registrar_usuario("Carlos López", "USER002")
    biblioteca.registrar_usuario("María Rodríguez", "USER003")
    print()

    # Prestar libros
    print("3. Prestando libros:")
    biblioteca.prestar_libro("978-8437604947", "USER001")  # Cien años de soledad a Ana
    biblioteca.prestar_libro("978-0451524935", "USER002")  # 1984 a Carlos
    biblioteca.prestar_libro("978-1451673319", "USER001")  # Fahrenheit 451 a Ana
    print()

    # Mostrar libros prestados
    print("4. Libros prestados a Ana García:")
    libros_ana = biblioteca.listar_libros_prestados_usuario("USER001")
    for libro in libros_ana:
        print(f"   - {libro}")
    print()

    # Buscar libros
    print("5. Búsqueda de libros:")
    print("   Buscando 'ciencia ficción':")
    resultados = biblioteca.buscar_por_categoria("Ciencia ficción")
    for libro in resultados:
        print(f"   - {libro}")

    print("\n   Buscando 'Orwell':")
    resultados = biblioteca.buscar_por_autor("Orwell")
    for libro in resultados:
        print(f"   - {libro}")
    print()

    # Devolver libro
    print("6. Devolviendo libro:")
    biblioteca.devolver_libro("978-1451673319", "USER001")  # Ana devuelve Fahrenheit 451
    print()

    # Intentar dar de baja usuario con libros prestados
    print("7. Intentando dar de baja a usuario con libros prestados:")
    biblioteca.dar_de_baja_usuario("USER001")
    print()

    # Listar todos los libros
    print("8. Todos los libros en la biblioteca:")
    todos_libros = biblioteca.listar_todos_libros()
    for libro in todos_libros:
        print(f"   - {libro}")
    print()

    print("=== FIN DE PRUEBAS ===")
    print(f"\nEstado final de la biblioteca: {biblioteca}")


# Ejecutar las pruebas si este archivo es el principal
if __name__ == "__main__":
    probar_sistema()