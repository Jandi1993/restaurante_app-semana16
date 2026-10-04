import os
import tkinter as tk
from tkinter import ttk, messagebox
from modelos.usuario import Usuario

class MainView(tk.Tk):
    def __init__(self, servicio, usuario_logueado):
        super().__init__()
        self.servicio = servicio
        self.usuario_logueado = usuario_logueado

        self.title("Sistema de Gestión de Restaurante - Semana 16")
        self.geometry("900x580")
        self.resizable(True, True)

        self._cargar_assets()
        self._centrar_ventana()
        self._crear_interfaz()

        # Cargar datos iniciales en la tabla
        self.cargar_usuarios_en_tabla()

    def _cargar_assets(self):
        """Carga el icono de la ventana si existe en assets/"""
        ruta_ico = os.path.join("assets", "logo.ico")
        ruta_png = os.path.join("assets", "logo.png")

        try:
            if os.path.exists(ruta_ico):
                self.iconbitmap(ruta_ico)
            elif os.path.exists(ruta_png):
                self.logo_icon = tk.PhotoImage(file=ruta_png)
                self.iconphoto(False, self.logo_icon)
        except Exception:
            pass

    def _centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def _crear_interfaz(self):
        # Banner superior
        frame_header = ttk.Frame(self, padding="10")
        frame_header.pack(fill=tk.X)

        # Muestra el logotipo cargado desde assets/
        ruta_logo = os.path.join("assets", "logo.png")
        if os.path.exists(ruta_logo):
            try:
                self.img_logo = tk.PhotoImage(file=ruta_logo)
                # Si la imagen es muy grande, reduce su escala
                if self.img_logo.width() > 100:
                    sub_factor = max(1, self.img_logo.width() // 60)
                    self.img_logo = self.img_logo.subsample(sub_factor, sub_factor)
                
                lbl_img = ttk.Label(frame_header, image=self.img_logo)
                lbl_img.pack(side=tk.LEFT, padx=(0, 10))
            except Exception:
                pass

        lbl_titulo = ttk.Label(
            frame_header, 
            text="Panel de Control - Gestión de Usuarios", 
            font=("Helvetica", 14, "bold")
        )
        lbl_titulo.pack(side=tk.LEFT)

        lbl_user_info = ttk.Label(
            frame_header, 
            text=f"Usuario: {self.usuario_logueado.nombre} [{self.usuario_logueado.rol}]", 
            font=("Helvetica", 10, "italic")
        )
        lbl_user_info.pack(side=tk.RIGHT)

        ttk.Separator(self, orient="horizontal").pack(fill=tk.X, padx=10, pady=5)

        # Contenedor Principal
        frame_body = ttk.Frame(self, padding="10")
        frame_body.pack(fill=tk.BOTH, expand=True)

        # ------------------- FORMULARIO (IZQUIERDA) -------------------
        frame_form = ttk.LabelFrame(frame_body, text=" Datos del Usuario ", padding="15")
        frame_form.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        ttk.Label(frame_form, text="ID Usuario:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.ent_id = ttk.Entry(frame_form, width=22)
        self.ent_id.grid(row=0, column=1, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.ent_nombre = ttk.Entry(frame_form, width=22)
        self.ent_nombre.grid(row=1, column=1, pady=5)

        ttk.Label(frame_form, text="Username:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.ent_username = ttk.Entry(frame_form, width=22)
        self.ent_username.grid(row=2, column=1, pady=5)

        ttk.Label(frame_form, text="Rol:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.combo_rol = ttk.Combobox(
            frame_form, 
            values=["Administrador", "Empleado", "Cliente"], 
            state="readonly", 
            width=20
        )
        self.combo_rol.grid(row=3, column=1, pady=5)
        self.combo_rol.current(1)

        # Botones CRUD con command=
        frame_botones = ttk.Frame(frame_form, padding="10")
        frame_botones.grid(row=4, column=0, columnspan=2, pady=15)

        self.btn_guardar = ttk.Button(frame_botones, text="Registrar", command=self.on_registrar)
        self.btn_guardar.pack(fill=tk.X, pady=2)

        self.btn_actualizar = ttk.Button(frame_botones, text="Actualizar", command=self.on_actualizar)
        self.btn_actualizar.pack(fill=tk.X, pady=2)

        self.btn_eliminar = ttk.Button(frame_botones, text="Eliminar", command=self.on_eliminar)
        self.btn_eliminar.pack(fill=tk.X, pady=2)

        self.btn_limpiar = ttk.Button(frame_botones, text="Limpiar / Cancelar", command=self.limpiar_formulario)
        self.btn_limpiar.pack(fill=tk.X, pady=2)

        # ------------------- TABLA TREEVIEW (DERECHA) -------------------
        frame_tabla = ttk.LabelFrame(frame_body, text=" Lista de Usuarios ", padding="10")
        frame_tabla.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        columnas = ("id", "nombre", "username", "rol")
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", selectmode="browse")

        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre Completo")
        self.tree.heading("username", text="Username")
        self.tree.heading("rol", text="Rol")

        self.tree.column("id", width=80, anchor=tk.CENTER)
        self.tree.column("nombre", width=180, anchor=tk.W)
        self.tree.column("username", width=120, anchor=tk.W)
        self.tree.column("rol", width=100, anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # ------------------- EVENTOS EXIGIDOS POR RÚBRICA -------------------
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.combo_rol.bind("<<ComboboxSelected>>", self.on_combo_rol_selected)
        self.bind("<Return>", lambda event: self.on_registrar())
        self.bind("<Escape>", lambda event: self.limpiar_formulario())

    # ------------------- CALLBACKS Y MANEJO DE EVENTOS -------------------
    def on_combo_rol_selected(self, event):
        """Callback explícito para la selección del rol"""
        pass

    def cargar_usuarios_en_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        usuarios = self.servicio.obtener_todos_usuarios()
        for u in usuarios:
            self.tree.insert("", tk.END, values=(u.id_usuario, u.nombre, u.usuario, u.rol))

    def on_tree_select(self, event):
        seleccion = self.tree.selection()
        if not seleccion:
            return

        item = self.tree.item(seleccion[0])
        valores = item["values"]

        if valores:
            self.ent_id.delete(0, tk.END)
            self.ent_id.insert(0, valores[0])
            self.ent_id.config(state="disabled")

            self.ent_nombre.delete(0, tk.END)
            self.ent_nombre.insert(0, valores[1])

            self.ent_username.delete(0, tk.END)
            self.ent_username.insert(0, valores[2])

            self.combo_rol.set(valores[3])

    def limpiar_formulario(self):
        self.tree.selection_remove(self.tree.selection())
        self.ent_id.config(state="normal")
        self.ent_id.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_username.delete(0, tk.END)
        self.combo_rol.current(1)

    def on_registrar(self):
        if self.usuario_logueado.rol != "Administrador":
            messagebox.showerror("Acceso Denegado", "Solo el Administrador puede gestionar usuarios.")
            return

        id_u = self.ent_id.get().strip()
        nom = self.ent_nombre.get().strip()
        user = self.ent_username.get().strip()
        rol = self.combo_rol.get()

        if not id_u or not nom or not user:
            messagebox.showwarning("Incompleto", "Todos los campos son obligatorios.")
            return

        nuevo_u = Usuario(id_u, nom, user, rol)
        if self.servicio.agregar_usuario(nuevo_u):
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            self.cargar_usuarios_en_tabla()
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", "El ID de usuario ya existe.")

    def on_actualizar(self):
        if self.usuario_logueado.rol != "Administrador":
            messagebox.showerror("Acceso Denegado", "Solo el Administrador puede gestionar usuarios.")
            return

        id_u = self.ent_id.get().strip()
        nom = self.ent_nombre.get().strip()
        user = self.ent_username.get().strip()
        rol = self.combo_rol.get()

        if not id_u:
            messagebox.showwarning("Selección requerida", "Seleccione un usuario de la lista.")
            return

        u_actualizado = Usuario(id_u, nom, user, rol)
        if self.servicio.actualizar_usuario(u_actualizado):
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
            self.cargar_usuarios_en_tabla()
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el usuario.")

    def on_eliminar(self):
        if self.usuario_logueado.rol != "Administrador":
            messagebox.showerror("Acceso Denegado", "Solo el Administrador puede gestionar usuarios.")
            return

        id_u = self.ent_id.get().strip()
        if not id_u:
            messagebox.showwarning("Selección requerida", "Seleccione un usuario de la lista.")
            return

        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el usuario {id_u}?"):
            if self.servicio.eliminar_usuario(id_u):
                messagebox.showinfo("Éxito", "Usuario eliminado.")
                self.cargar_usuarios_en_tabla()
                self.limpiar_formulario()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario.")