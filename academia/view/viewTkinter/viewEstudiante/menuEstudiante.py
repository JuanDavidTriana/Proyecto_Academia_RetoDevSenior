import customtkinter as ctk


class MenuEstudiante():
    def __init__(self,db = None, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Menu Estudiante")

        #Configurar el tema de la ventana
        ctk.set_appearance_mode(tema_actual)

        #Configuracion de cierra de ventana
        self.root.protocol("WM_DELETE_WINDOW", self.regresar_menu_principal)

        #Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        #Asignar tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.3)
        alto_ventana = int(alto_pantalla * 0.45)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        #Configuraracion de restricciones de la ventana
        self.root.resizable(False, False)

        #Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Menu Estudiante", font=("Arial", 16))
        self.titulo.pack(pady=10)

        #Boton para cambiar el tema de la ventana
        self.tema_actual = "System"
        self.btn_cambiar_tema = ctk.CTkButton(self.root, text="Cambiar Tema", command=self.cambiar_tema)
        self.btn_cambiar_tema.pack(pady=10)

        #Boton para listar estudiantes en un ventana emergente que tenga una tabla
        self.btn_listar_estudiantes = ctk.CTkButton(self.root, text="Listar Estudiantes", command=self.listar_estudiantes)
        self.btn_listar_estudiantes.pack(pady=10)

        #Boton para registrar estudiante
        self.btn_registrar_estudiante = ctk.CTkButton(self.root, text="Registrar Estudiante", command=self.registrar_estudiante)
        self.btn_registrar_estudiante.pack(pady=10)

        #Boton para actualizar estudiante
        self.btn_actualizar_estudiante = ctk.CTkButton(self.root, text="Actualizar Estudiante", command=self.actualizar_estudiante)
        self.btn_actualizar_estudiante.pack(pady=10)

        #Boton para eliminar estudiante
        self.btn_eliminar_estudiante = ctk.CTkButton(self.root, text="Eliminar Estudiante", command=self.eliminar_estudiante)
        self.btn_eliminar_estudiante.pack(pady=10)

        #Crear un boton para regresar al menu principal
        self.btn_regresar = ctk.CTkButton(self.root, text="Regresar", command=self.regresar_menu_principal)
        self.btn_regresar.pack(pady=10)

    def regresar_menu_principal(self):
        from view.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop()

    def cambiar_tema(self):
        if self.tema_actual == "Light":
            ctk.set_appearance_mode("Dark")
            self.tema_actual = "Dark"
        else:
            ctk.set_appearance_mode("Light")
            self.tema_actual = "Light"

    def listar_estudiantes(self):
        from view.viewTkinter.viewEstudiante.listarEstudiantes import ListarEstudiantes
        listar_estudiantes = ListarEstudiantes(db = self.db, tema_actual = self.tema_actual)
        listar_estudiantes.root.mainloop()

    def registrar_estudiante(self):
        from view.viewTkinter.viewEstudiante.registrarEstudiante import RegistrarEstudiante
        registrar_estudiante = RegistrarEstudiante(db = self.db, tema_actual = self.tema_actual)
        registrar_estudiante.root.mainloop()

    def eliminar_estudiante(self):
        from view.viewTkinter.viewEstudiante.eliminarEstudiante import EliminarEstudiante
        eliminar_estudiante = EliminarEstudiante(db = self.db, tema_actual = self.tema_actual)
        eliminar_estudiante.root.mainloop()

    def actualizar_estudiante(self):
        from view.viewTkinter.viewEstudiante.actualizarEstudiante import ActualizarEstudiante
        actualizar_estudiante = ActualizarEstudiante(db = self.db, tema_actual = self.tema_actual)
        actualizar_estudiante.root.mainloop()

