# Restaurante App - Semana 16

## Descripción
Evolución del sistema de gestión de restaurante implementando un CRUD completo para la gestión de usuarios con control de roles y persistencia de datos en formato JSON.

## Funcionalidades Semana 16
- *Modelo de Usuario:* Inclusión del atributo rol (Administrador, Empleado, Cliente) y persistencia en datos/usuarios.json.
- *Gestión Básica (CRUD):* Registro, consulta, actualización y eliminación de usuarios desde la interfaz gráfica.
- *Eventos Bindings en Tkinter:*
  - <<TreeviewSelect>>: Carga los datos del usuario seleccionado directamente en el formulario.
  - <<ComboboxSelected>>: Manejo de selección dinámica en el combobox de roles.
  - <Return>: Registrar usuario con tecla Enter.
  - <Escape>: Limpiar formulario / Cancelar.
- *Validaciones:* Control de permisos según el rol del usuario autenticado.
- *Recursos Visuales:* Integración de assets gráficos desde la carpeta assets/.

## Estructura del Proyecto
restaurante_app/
│
├── assets/             # Recursos de imágenes e iconos
├── datos/              # Persistencia en archivos JSON
├── modelos/            # Clases y objetos del dominio (Usuario, Producto)
├── servicios/          # Lógica de negocio y manejo de archivos
├── ui/                 # Interfaz gráfica (Login, MainView)
├── main.py             # Punto de entrada de la aplicación
└── README.md           # Documentación del proyecto