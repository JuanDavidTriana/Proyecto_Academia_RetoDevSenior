from config.database import Database
from models.estudiante import Estudiante

class EstudianteController:
    def __init__(self, db):
        self.db = db

    def registrar_estudiante(self, nombre, apellido, correo, telefono):
        """
        Registra un estudiante en la base de datos.

        :param nombre: nombre del estudiante
        :param apellido: apellido del estudiante
        :param correo: correo electr nico del estudiante
        :param telefono: tel fono del estudiante
        """
        sql = """
            INSERT INTO Estudiantes (nombre, apellido, correo_electronico, telefono)
            VALUES (%s, %s, %s, %s)
        """
        params = (nombre, apellido, correo, telefono)
        self.db.execute_query(sql, params)

    def listar_estudiantes(self):
        """
        Devuelve una lista de objetos Estudiante que representan a los estudiantes
        registrados en la base de datos.
        """
        sql = """
        SELECT id_estudiante, nombre, apellido, correo_electronico, telefono FROM estudiantes"
        """
        resultados = self.db.execute_select(sql)
        return [Estudiante(*resultado) for resultado in resultados]