import os
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    """Servicio encargado de administrar los usuarios y sincronizarlos con datos/usuarios.json"""

    def __init__(self, ruta_json="datos/usuarios.json"):
        self.ruta_json = ruta_json
        self.usuarios = []
        self.cargar_usuarios()

    def cargar_usuarios(self):
        """Lee el archivo JSON utilizando ArchivoServicio y mapea los datos a la lista de usuarios."""
        datos = ArchivoServicio.leer_json(self.ruta_json)
        self.usuarios = [Usuario.from_dict(u) for u in datos]

    def guardar_usuarios(self):
        """Persiste la lista actual de usuarios en el archivo JSON."""
        datos = [u.to_dict() for u in self.usuarios]
        return ArchivoServicio.guardar_json(self.ruta_json, datos)

    def obtener_todos_usuarios(self):
        return self.usuarios

    def obtener_usuario_por_username(self, username):
        for u in self.usuarios:
            if u.usuario == username:
                return u
        return None

    def buscar_usuario_por_id(self, id_usuario):
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                return u
        return None

    def agregar_usuario(self, nuevo_usuario):
        if self.buscar_usuario_por_id(nuevo_usuario.id_usuario):
            return False

        self.usuarios.append(nuevo_usuario)
        self.guardar_usuarios()
        return True

    def actualizar_usuario(self, usuario_actualizado):
        for i, u in enumerate(self.usuarios):
            if u.id_usuario == usuario_actualizado.id_usuario:
                self.usuarios[i] = usuario_actualizado
                self.guardar_usuarios()
                return True
        return False

    def eliminar_usuario(self, id_usuario):
        usr = self.buscar_usuario_por_id(id_usuario)
        if usr:
            self.usuarios.remove(usr)
            self.guardar_usuarios()
            return True
        return False