from modelo.libro import Libro
from modelo.carro_compra import CarroCompras
from modelo.libro_existente_error import LibroExistenteError
from modelo.libro_agotado_error import LibroAgotadoError
from modelo.existencias_insuficientes_error import ExistenciasInsuficientesError

class TiendaLibros:
    # Defina metodo inicializador __init__
    def __init__(self):
        self.catalogo: dict = {}
        self.carrito = CarroCompras()
        
    # Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int) -> Libro():
        if isbn in self.catalogo:
            raise LibroExistenteError()
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro
    
    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, isbn, cantidad_unidades: int):
        if isbn not in self.catalogo:
            raise LibroAgotadoError()
        libro = self.catalogo[isbn]
        if cantidad_unidades > libro.existencias:
            raise ExistenciasInsuficientesError
        CarroCompras.agregar_item(libro, cantidad_unidades)


    # Defina metodo retirar_item_de_carrito
    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)