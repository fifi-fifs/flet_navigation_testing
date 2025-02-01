#  ##   ###
import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors
#  ##   ###


def main(page: Page):
    page.title = "Routes Example"

    def route_change(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Flet app"), bgcolor=colors.SURFACE_CONTAINER_HIGHEST),
                    ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                View(
                    "/store",
                    [
                        AppBar(title=Text("Store"), bgcolor=colors.SURFACE_CONTAINER_HIGHEST),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        if page.route == "/erre":
            page.views.append(
                View(
                    "/erre",
                    [
                        AppBar(title=Text("This is Erre", size=24,  color='blue', weight='bold'), bgcolor=colors.RED,),
                        ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


if __name__ == "__main__":
    flet.app(target= main, view=flet.AppView.WEB_BROWSER)
    # flet.app(target= main)