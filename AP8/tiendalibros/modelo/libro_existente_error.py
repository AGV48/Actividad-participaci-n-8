from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError

class LibroExistenteError(LibroError):
    # Defina metodo inicializador
    def __init__(self):
        super().__init__()
    
    # Defina metodo especial
    def __str__(self) -> str:
        return (f"El libro con titulo {Libro.titulo} y isbn: {Libro.isbn} ya existe en el catalogo")
