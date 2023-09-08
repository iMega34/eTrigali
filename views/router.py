
import flet as ft

from views.home import Home


class Router:
    """
    Contiene las rutas de la aplicación y cambia la vista de la página web.
    """

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.routes = {
            "/": Home(page),                        # Página de inicio
            # "/cashier": Cashier(page),              # Página de caja
            # "/orders": Orders(page),                # Página de órdenes
            # "/digital_menu": DigitalMenu(page),     # Página de menú digital
        }
        # Página y ruta predeterminadas del router
        self.view = ft.Container(
            content = self.routes["/"],
            expand = True
        )

    def route_change(self, route: str) -> None:
        """
        Cambia la ruta del router y actualiza la página web.

        :param:`route` Ruta a la que se desea cambiar como string
        """
        self.view.content = self.routes[route.route]
        self.view.update()