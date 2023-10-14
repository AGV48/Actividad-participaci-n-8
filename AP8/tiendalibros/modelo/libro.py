class Libro:
    def __init__(self, isbn: str, titulo: str, precio: float, existencias: int):
        self.isbn: str = isbn
        self.titulo: str = titulo
        self.precio: float = precio
        self.existencias: int = existencias

    def __str__(self):
        return "({}) {} - ${:,.2f}".format(self.isbn, self.titulo, self.precio)
