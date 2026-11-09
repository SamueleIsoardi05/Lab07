import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_biblioteca(self):
        nomi = self._model.get_biblioteche()
        print(f"[DEBUG CONTROLLER] Ricevuti dal Model: {nomi}")
        options = [ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro")]

        # 2. Converte i nomi in opzioni grafiche per Flet (passando SOLO il campo text)
        options.extend([ft.dropdown.Option(key=str(nome), text=str(nome)) for nome in nomi])
        print(f"[DEBUG CONTROLLER] Create {len(options)} opzioni Flet")
        self._view.dd_biblioteche.options = options
        self._view.dd_biblioteche.update()

    def popola_generi(self):
        generi = self._model.get_generi()
        options = [ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro")]
        options.extend([ft.dropdown.Option(key=str(g), text=str(g)) for g in generi])

        self._view.dd_generi.options = options
        self._view.dd_generi.update()

    # CALLBACKS DROPDOWN
    # TODO
    def read_biblioteca(self, e):
        """Salva la biblioteca scelta dall'utente quando cambia la selezione."""
        valore = e.control.value
        if valore == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = valore

    def read_genere(self, e):
        """Salva il genere scelto dall'utente quando cambia la selezione."""
        valore = e.control.value
        if valore == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore


    # AZIONE: MOSTRA LIBRI
    # TODO
    def handle_mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        if self.biblioteca_selezionata is None and self.genere_selezionato is None:
            self._view.alert.show_alert("Nessun libro trovato con i criteri selezionati")
        else:

            if not libri:
                self._view.alert.show_alert("Nessun libro trovato con i criteri selezionati")
            else:
                for l in libri:
                    self._view.lv_libri.controls.append(
                        ft.Text(f"• {l.titolo} — Autore: {l.autore} | Genere: {l.genere}")
                    )
                self._view.lv_libri.update()
        self._view.lv_libri.controls.clear()
