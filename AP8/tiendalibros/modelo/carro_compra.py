from modelo.item_compra import ItemCompra
class CarroCompras:
    # Defina metodo inicializador __init__(self)
    def __init__(self):
        self.item: list[ItemCompra] = []
    
    # Defina el metodo agregar_item
    def agregar_item(self, libro, cantidad_libro):
        nuevo_item: ItemCompra = ItemCompra(libro, cantidad_libro)
        self.item.append(nuevo_item)
        return nuevo_item

    # Defina el metodo calcular_total
    def calcular_total(self):
        total = 0
        for item in self.item:
            total += item.calcular_subtotal()
        return total
    
    # Defina el metodo quitar_item
    def quitar_item(self, isbn):
        self.item = [item for item in self.item if isbn != item.libro.isbn]
        return
    
