import customtkinter as ctk
from tkinter import ttk, messagebox  # Importamos ttk para usar Treeview y messagebox para confirmación
from controllers.estudiante_controller import EstudianteController
from mysql.connector import IntegrityError

class ListarEstudiantes:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Listar Estudiantes")
        self.estudiante_controller = EstudianteController(db)

        # Configurar el tema de la ventana
        ctk.set_appearance_mode(tema_actual)

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.4)
        alto_ventana = int(alto_pantalla * 0.4) 
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        # Configuración de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana   
        self.titulo = ctk.CTkLabel(self.root, text="Listar Estudiantes", font=("Arial", 16))
        self.titulo.pack(pady=10)

        # Crear un frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.root)
        self.frame_tabla.pack(pady=10)

        # Crear la tabla (usando Treeview de tkinter)
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "Nombre", "Apellido", "Correo", "Telefono"), show="headings")
        self.tabla.pack(expand=True, fill="both")

        # Configurar encabezados
        self.tabla.heading("ID", text="ID Estudiante")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellido", text="Apellido")
        self.tabla.heading("Correo", text="Correo")
        self.tabla.heading("Telefono", text="Teléfono")

        # Ajustar el ancho de las columnas
        self.tabla.column("ID", width=100)
        self.tabla.column("Nombre", width=150)
        self.tabla.column("Apellido", width=150)
        self.tabla.column("Correo", width=200)
        self.tabla.column("Telefono", width=120)


        # Cargar los datos de la tabla
        self.cargar_datos_tabla()

    def cargar_datos_tabla(self):
        try:
            estudiantes = self.estudiante_controller.listar_estudiantes()
            # Limpiar la tabla antes de cargar nuevos datos
            for row in self.tabla.get_children():
                self.tabla.delete(row)
            
            for estudiante in estudiantes:
                # Insertar filas en la tabla
                self.tabla.insert("", "end", values=(estudiante.id_estudiante, estudiante.nombre, estudiante.apellido, estudiante.correo, estudiante.telefono))

        except IntegrityError as e:
            print(f"Error al cargar los datos: {e}")
            # Aquí podrías mostrar un mensaje de error en la interfaz si lo deseas

    def regresar_menu_principal(self):
        from view.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(db=self.db, tema_actual=self.tema_actual)
        menu_principal.root.mainloop()

