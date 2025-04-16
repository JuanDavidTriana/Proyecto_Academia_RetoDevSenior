from view.menu import menu_principal
from config.database import Database

if __name__ == "__main__":
    db = Database()
    try:
        menu_principal(db)
    finally:
        db.close()