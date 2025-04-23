import customtkinter as ctk


class MenuDocente():
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Menu Docente")

        #Configurar el tema de la ventana
        ctk.set_appearance_mode(tema_actual)

        #Configuracion de cierra de ventana
        self.root.protocol("WM_DELETE_WINDOW", self.regresar_menu_principal)

        #Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        #Asignar tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.4)
        alto_ventana = int(alto_pantalla * 0.6)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        #Configuraracion de restricciones de la ventana
        self.root.resizable(False, False)

        #Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Menu Docente", font=("Arial", 16))
        self.titulo.pack(pady=20)

        #Boton para cambiar el tema de la ventana
        self.tema_actual = tema_actual
        self.btn_cambiar_tema = ctk.CTkButton(self.root, text="Cambiar Tema", command=self.cambiar_tema)
        self.btn_cambiar_tema.pack(pady=10, padx=20, anchor="w")

        #Boton para listar docentes
        self.btn_listar_docentes = ctk.CTkButton(self.root, text="Listar Docentes", command=self.listar_docentes)
        self.btn_listar_docentes.pack(pady=10, padx=20, anchor="w")

        #Boton para registrar docente
        self.btn_registrar_docente = ctk.CTkButton(self.root, text="Registrar Docente", command=self.registrar_docente)
        self.btn_registrar_docente.pack(pady=10, padx=20, anchor="w")

        #Boton para actualizar docente
        self.btn_actualizar_docente = ctk.CTkButton(self.root, text="Actualizar Docente", command=self.actualizar_docente)
        self.btn_actualizar_docente.pack(pady=10, padx=20, anchor="w")

        #Boton para eliminar docente
        self.btn_eliminar_docente = ctk.CTkButton(self.root, text="Eliminar Docente", command=self.eliminar_docente)
        self.btn_eliminar_docente.pack(pady=10, padx=20, anchor="w")

        #Crear un boton para regresar al menu principal
        self.btn_regresar = ctk.CTkButton(self.root, text="Regresar", command=self.regresar_menu_principal)
        self.btn_regresar.pack(pady=20, padx=20, anchor="w")

    def regresar_menu_principal(self):
        from view.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(db=self.db, tema_actual=self.tema_actual)
        menu_principal.root.mainloop()

    def cambiar_tema(self):
        if self.tema_actual == "Light":
            ctk.set_appearance_mode("Dark")
            self.tema_actual = "Dark"
        else:
            ctk.set_appearance_mode("Light")
            self.tema_actual = "Light"

    def listar_docentes(self):
        from view.viewTkinter.viewDocente.listarDocentes import ListarDocentes
        listar_docentes = ListarDocentes(db=self.db, tema_actual=self.tema_actual)
        listar_docentes.root.mainloop()

    def registrar_docente(self):
        from view.viewTkinter.viewDocente.registrarDocente import RegistrarDocente
        registrar_docente = RegistrarDocente(db=self.db, tema_actual=self.tema_actual)
        registrar_docente.root.mainloop()

    def actualizar_docente(self):
        from view.viewTkinter.viewDocente.actualizarDocente import ActualizarDocente
        actualizar_docente = ActualizarDocente(db=self.db, tema_actual=self.tema_actual)
        actualizar_docente.root.mainloop()

    def eliminar_docente(self):
        from view.viewTkinter.viewDocente.eliminarDocente import EliminarDocente
        eliminar_docente = EliminarDocente(db=self.db, tema_actual=self.tema_actual)
        eliminar_docente.root.mainloop()
