from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def read_libri_from_db(self):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is not None:
            query = "SELECT * FROM libro"
            cursor = cnx.cursor()
            cursor.execute(query)

            for row in cursor:
                libro = Libro(*row)
                result.append(libro)

            cursor.close()
            cnx.close()

        return result

    def read_libri_filtrati(self, id_biblioteca=None, genere=None):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is not None:
            # Query con JOIN per filtrare sia per nome biblioteca che per genere
            query = """
                SELECT * 
                FROM libro 
                WHERE id_biblioteca=COALESCE(%s, id_biblioteca) 
                AND genere=COALESCE(%s, genere)
            """
            cursor = cnx.cursor()
            cursor.execute(query, (id_biblioteca, genere))

            for row in cursor:
                libro = Libro(*row)
                result.append(libro)

            cursor.close()
            cnx.close()



        return result