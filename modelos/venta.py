class Venta:
    def __init__(self, id_venta, id_usuario, total, fecha):
        self.id_venta = id_venta
        self.id_usuario = id_usuario
        self.total = float(total)
        self.fecha = fecha

    def to_dict(self):
        """Convierte la entidad Venta a un diccionario para su persistencia en JSON."""
        return {
            "id_venta": self.id_venta,
            "id_usuario": self.id_usuario,
            "total": self.total,
            "fecha": self.fecha
        }

    @staticmethod
    def from_dict(data):
        """Crea una instancia de Venta a partir de los datos leídos del archivo JSON."""
        return Venta(
            id_venta=data.get("id_venta", ""),
            id_usuario=data.get("id_usuario", ""),
            total=data.get("total", 0.0),
            fecha=data.get("fecha", "")
        )