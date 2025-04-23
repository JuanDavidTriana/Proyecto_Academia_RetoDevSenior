import customtkinter as ctk
from tkinter import ttk
from controllers.docente_controller import DocenteController
from mysql.connector import IntegrityError

class ListarDocentes:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Listar Docentes")
        self.docente_controller = DocenteController(db)

        # Configurar el tema de la ventana
        ctk.set_appearance_mode(tema_actual)

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.8)
        alto_ventana = int(alto_pantalla * 0.7)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        # Configuración de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana   
        self.titulo = ctk.CTkLabel(self.root, text="Listar Docentes", font=("Arial", 16))
        self.titulo.pack(pady=20)

        # Crear un frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.root)
        self.frame_tabla.pack(pady=10, padx=40, fill="both", expand=True)

        # Crear la tabla (usando Treeview de tkinter)
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "Nombre", "Apellido", "Correo", "Telefono", "Especialidad"), show="headings")
        self.tabla.pack(expand=True, fill="both", padx=20)

        # Configurar encabezados
        self.tabla.heading("ID", text="ID Docente")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellido", text="Apellido")
        self.tabla.heading("Correo", text="Correo")
        self.tabla.heading("Telefono", text="Teléfono")
        self.tabla.heading("Especialidad", text="Especialidad")

        # Ajustar el ancho de las columnas
        self.tabla.column("ID", width=150)
        self.tabla.column("Nombre", width=250)
        self.tabla.column("Apellido", width=250)
        self.tabla.column("Correo", width=300)
        self.tabla.column("Telefono", width=200)
        self.tabla.column("Especialidad", width=250)

        # Crear un frame para los botones
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(pady=20, padx=40)

        # Botón para regresar al menú principal
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", command=self.regresar_menu_principal)
        self.btn_regresar.pack(side="left", padx=10)

        # Cargar los datos de la tabla
        self.cargar_datos_tabla()

    def cargar_datos_tabla(self):
        try:
            docentes = self.docente_controller.listar_docentes()
            # Limpiar la tabla antes de cargar nuevos datos
            for row in self.tabla.get_children():
                self.tabla.delete(row)
            
            for docente in docentes:
                # Insertar filas en la tabla
                self.tabla.insert("", "end", values=(
                    docente.id_docente, 
                    docente.nombre, 
                    docente.apellido, 
                    docente.correo, 
                    docente.telefono,
                    docente.especialidad
                ))

        except IntegrityError as e:
            print(f"Error al cargar los datos: {e}")
            # Aquí podrías mostrar un mensaje de error en la interfaz si lo deseas

    def regresar_menu_principal(self):
        from view.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(db=self.db, tema_actual=self.tema_actual)
        menu_principal.root.mainloop() 