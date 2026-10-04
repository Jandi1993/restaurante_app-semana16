import json
import os

class ArchivoServicio:
    """Servicio genérico para lectura y escritura de archivos JSON."""

    @staticmethod
    def leer_json(ruta):
        """Lee un archivo JSON y retorna una lista o diccionario con los datos."""
        if not os.path.exists(ruta):
            return []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, Exception):
            return []

    @staticmethod
    def guardar_json(ruta, datos):
        """Guarda los datos en formato JSON en la ruta especificada."""
        try:
            directorio = os.path.dirname(ruta)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio, exist_ok=True)
                
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar el archivo {ruta}: {e}")
            return False