import flet as ft
from UI.alert import AlertManager
'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        self.dd_biblioteche = ft.Dropdown(label="Biblioteche",
                                          width=350,
                                          value="Nessun filtro",
                                          on_select = self.controller.read_biblioteca)

        self.dd_generi = ft.Dropdown(label="Generi",
                                     width=200,
                                     value= "Nessun filtro",
                                     on_select=self.controller.read_genere
                                     )

        # Sezione 3: Libri
        # TODO
        self.btn_libri= ft.Button(content="Mostra Libri", on_click=self.controller.handle_mostra_libri)
        self.lv_libri = ft.ListView(
            expand=True,
            spacing=10,
            padding=10)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO

            ft.Row(spacing= 40,
                   controls=[self.dd_biblioteche, self.dd_generi],
                   alignment = ft.MainAxisAlignment.CENTER),
            ft.Divider(),
            ft.Container(height=20),
            # Sezione 3: Libri
            # TODO
            ft.Row(controls=[self.btn_libri], alignment = ft.MainAxisAlignment.CENTER),
            ft.Container(height=20),
            self.lv_libri
        )

        self.page.scroll = "adaptive"

        if self.controller:
            self.controller.popola_biblioteca()
            self.controller.popola_generi()

        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
