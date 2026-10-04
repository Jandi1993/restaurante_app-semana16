class Usuario:
    def __init__(self, id_usuario, nombre, usuario, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.usuario = usuario
        self.rol = rol

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(data):
        return Usuario(
            id_usuario=data.get("id_usuario", data.get("id", "")),
            nombre=data.get("nombre", ""),
            usuario=data.get("usuario", data.get("username", "")),
            rol=data.get("rol", "Empleado")
        )