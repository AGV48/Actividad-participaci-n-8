import sys
from tiendalibros.modelo.tienda_libros import TiendaLibros
from modelo.libro_error import LibroError

class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    # Defina el metodo retirar_libro_de_carrito_de_compras
    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea retirar del carrito de compras: ")
        try:
            self.tienda_libros.retirar_item_de_carrito(isbn)
            print("El libro ha sido eliminado del carrito exitosamente")
        except LibroError as e:
            print("error: ", str(e))

    # Defina el metodo agregar_libro_a_carrito_de_compras
    def agregar_libro_a_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea agregar al carrito de compras: ")
        cantidad_unidades = int(input("Ingrese la cantidad de ese libro que desea llevar: "))
        try:
            self.tienda_libros.agregar_libro_a_carrito(isbn, cantidad_unidades)
            print("El libro fue agregado exitosamente")
        except LibroError as e:
            print("error: ", str(e))

    # Defina el metodo adicionar_un_libro_a_catalogo
    def adicionar_un_libro_a_catalogo(self):
        isbn = input("Ingrese el ISBN del libro que desea agregar al catalogo: ")
        titulo = input("Ingrese el titulo del libro que desea agregar al catalogo: ")
        precio = float(input("Ingrese el precio del libro que desea agregar al catalogo: "))
        existencias = int(input("Ingrese la cantidad de existencias del libro que desea agregar al catalogo: "))
        try:
            self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print("Libro agregado exitosamente")
        except LibroError as e:
            print("error: ", str(e))