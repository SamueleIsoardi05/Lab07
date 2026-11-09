from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        # 1. Recuperiamo tutti i libri e tutte le biblioteche dal DB
        libri = self._libro_dao.read_libri_from_db()
        biblioteche = self._biblioteca_dao.read_biblioteche_from_db()

        # 2. Se l'utente ha selezionato una biblioteca specifica (non "Nessun filtro"), trovale l'ID
        id_biblio_selezionata = None
        if biblioteca:
            for b in biblioteche:
                if b.nome == biblioteca:
                    id_biblio_selezionata = b.id
                    break

        # 3. Filtraggio della lista con ciclo Python
        libri_filtrati = []
        for l in libri:
            # Condizione Biblioteca: vera se l'utente non ha messo il filtro OR se l'ID coincide
            condizione_biblio = (id_biblio_selezionata is None) or (l.id_biblioteca == id_biblio_selezionata)

            # Condizione Genere: vera se l'utente non ha messo il filtro OR se il genere coincide
            condizione_genere = (genere is None) or (l.genere == genere)

            # Se entrambe le condizioni sono soddisfatte, aggiungiamo il libro
            if condizione_biblio and condizione_genere:
                libri_filtrati.append(l)

        return libri_filtrati

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        libri = self._libro_dao.read_libri_from_db()
        # Estraiamo solo il campo .nome
        # 1. Creiamo una lista vuota per contenere solo i nomi

        generi = set([l.genere for l in libri ])
        return sorted(list(generi))


    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        # Prende l'elenco degli oggetti Biblioteca dal DAO
        biblioteche = self._biblioteca_dao.read_biblioteche_from_db()

        # Estraiamo solo il campo .nome
        # 1. Creiamo una lista vuota per contenere solo i nomi
        nomi = [b.nome for b in biblioteche]

        # 2. Cicliamo su ogni elemento della lista 'biblioteche' (restituita dal DAO)
        print(f"[DEBUG MODEL] Nomi trovati: {nomi}")  # <--- PRINT DI CONTROL

        # 4. Restituiamo la lista di stringhe
        return nomi
