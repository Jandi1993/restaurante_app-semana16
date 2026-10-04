import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(tk.Tk):
    def __init__(self, servicio, on_login_success):
        super().__init__()
        self.servicio = servicio
        self.on_login_success = on_login_success

        self.title("Iniciar Sesión - Restaurante App")
        self.geometry("380x300")
        self.resizable(False, False)

        self._crear_widgets()
        self._centrar_ventana()

    def _centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def _crear_widgets(self):
        frame_main = ttk.Frame(self, padding="20")
        frame_main.pack(fill=tk.BOTH, expand=True)

        lbl_titulo = ttk.Label(
            frame_main, 
            text="Acceso al Sistema", 
            font=("Helvetica", 14, "bold")
        )
        lbl_titulo.pack(pady=(0, 20))

        # Campo Usuario
        lbl_usuario = ttk.Label(frame_main, text="Nombre de Usuario:")
        lbl_usuario.pack(anchor=tk.W, pady=(5, 2))
        self.ent_usuario = ttk.Entry(frame_main, width=30)
        self.ent_usuario.pack(fill=tk.X, pady=(0, 15))
        self.ent_usuario.focus()

        # Botón Iniciar Sesión
        btn_ingresar = ttk.Button(
            frame_main, 
            text="Iniciar Sesión", 
            command=self.validar_login
        )
        btn_ingresar.pack(fill=tk.X, pady=(10, 5))

        # Evento de teclado (Enter) para iniciar sesión rápido
        self.bind("<Return>", lambda event: self.validar_login())

    def validar_login(self):
        nombre_usuario = self.ent_usuario.get().strip()

        if not nombre_usuario:
            messagebox.showwarning(
                "Campo Requerido", 
                "Por favor, ingrese un nombre de usuario.", 
                parent=self
            )
            return

        usuario_encontrado = self.servicio.obtener_usuario_por_username(nombre_usuario)

        if usuario_encontrado:
            messagebox.showinfo(
                "Éxito", 
                f"Bienvenido/a {usuario_encontrado.nombre} ({usuario_encontrado.rol})", 
                parent=self
            )
            self.destroy()
            self.on_login_success(usuario_encontrado)
        else:
            messagebox.showerror(
                "Error de Acceso", 
                "Usuario no registrado en el sistema.", 
                parent=self
            )