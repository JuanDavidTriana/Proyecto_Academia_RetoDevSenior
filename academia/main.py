from view.menu import menu_principal
from view.menuDocente import menu_principal_docente
from view.menuCurso import menu_principal_curso
from view.menuHorario import menu_principal_horario
from config.database import Database

if __name__ == "__main__":
    db = Database()
    try:
        #menu_principal(db) Menu de estudiantes
        #menu_principal_docente(db) #Menu de docentes
        #menu_principal_curso(db) #Menu de cursos
        menu_principal_horario(db) #Menu de horarios
        
    finally:
        db.close()