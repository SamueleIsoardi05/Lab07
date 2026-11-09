from typing import Any

import database.DB_connect
from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO

    def read_biblioteche_from_db(self):

        cnx = DBConnect.get_connection()
        result = []

        if cnx is not None:
            print("Connection established")

            query = "SELECT * FROM biblioteca"
            cursor = cnx.cursor()
            cursor.execute(query)

            for row in cursor:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)

            cursor.close()
            cnx.close()
            print("Biblioteche read from database")

        return result