from tiendalibros.modelo.libro import Libro


class LibroError(Exception):
    def __init__(self, libro: Libro):
        self.libro = libro
