class Producto:
    def __init__(self, id_producto, nombre, precio, categoria):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = float(precio)
        self.categoria = categoria

    def to_dict(self):
        """Convierte el objeto Producto a un diccionario para guardarlo en productos.json."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Producto a partir de un diccionario leído del JSON."""
        return Producto(
            id_producto=data.get("id_producto", ""),
            nombre=data.get("nombre", ""),
            precio=data.get("precio", 0.0),
            categoria=data.get("categoria", "")
        )