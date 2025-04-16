from view.menu import menu_principal
from view.menuDocente import menu_principal_docente
from config.database import Database

if __name__ == "__main__":
    db = Database()
    try:
        #menu_principal(db) Menu de estudiantes
        menu_principal_docente(db) #Menu de docentes
    finally:
        db.close()