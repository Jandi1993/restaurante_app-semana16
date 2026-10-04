import os
import tkinter as tk
from tkinter import messagebox
from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio
from ui.main_view import MainView

def main():
    # Inicialización del servicio de datos
    servicio = RestauranteServicio()

    # Usuario de prueba en sesión (Administrador para permitir el acceso a la gestión)
    # En producción provendría del flujo de LoginView
    usuario_admin = Usuario(
        id_usuario="ADM-001",
        nombre="Administrador Sistema",
        usuario="admin",
        rol="Administrador"
    )

    try:
        app = MainView(servicio=servicio, usuario_logueado=usuario_admin)
        
        # Cargar icono de la aplicación si existe en assets/
        ruta_icono = os.path.join("assets", "icono.ico")
        if os.path.exists(ruta_icono):
            app.iconbitmap(ruta_icono)

        app.mainloop()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")

if __name__ == "__main__":
    main()