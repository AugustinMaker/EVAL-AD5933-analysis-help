from interface import interface
import os
'''
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        clear_console()
        resultat = interface()
        if resultat == 1:
            print("programe cloturé")
            break
'''
from conversion import conversion
import flet as ft
from flet import Page, View, AppBar, Text, ElevatedButton, colors

def main(page: Page):
    print("Initial route:", page.route)
    history_stack = []

    def pick_files_result(e: ft.FilePickerResultEvent):
        file_paths = [f.path for f in e.files]
        selected_files.value = (
            ", ".join([f.name for f in e.files]) if e.files else "Cancelled!"
        )
        selected_files.update()
        conversion(file_paths)  # Appel de la fonction conversion avec les fichiers sélectionnés

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    def create_app_bar(title):
        return AppBar(
            title=Text(title),
            bgcolor=colors.SURFACE_VARIANT,
            leading=ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                on_click=go_back,
            ) if history_stack else None,
        )

    def go_back(e):
        if history_stack:
            last_route = history_stack.pop()
            page.go(last_route)

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()

        if page.route == "/":
            page.views.append(
                View("/", [
                    create_app_bar("Analysis Help for EVAL AD5933"),
                    ElevatedButton("Format Files", on_click=open_format),
                    ElevatedButton("Plot graph", on_click=open_settings),
                    ElevatedButton("Peak analysis", on_click=open_settings)
                ])
            )
        elif page.route == "/format":
            page.views.append(
                View("/format", [
                    create_app_bar("Format"),
                    Text("Welcome format", style="bodyMedium"),
                    ElevatedButton(
                        "Pick files",
                        icon=ft.icons.UPLOAD_FILE,
                        on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True)
                    ),
                    selected_files
                ])
            )
        elif page.route == "/settings":
            page.views.append(
                View("/settings", [
                    create_app_bar("Settings"),
                    Text("Settings!", style="bodyMedium"),
                    ElevatedButton("Go to mail settings", on_click=open_mail_settings)
                ])
            )
        elif page.route == "/settings/mail":
            page.views.append(
                View("/settings/mail", [
                    create_app_bar("Mail Settings"),
                    Text("Mail settings!")
                ])
            )
        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)

    def open_mail_settings(e):
        history_stack.append(page.route)
        page.go("/settings/mail")

    def open_settings(e):
        history_stack.append(page.route)
        page.go("/settings")

    def open_format(e):
        history_stack.append(page.route)
        page.go("/format")

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Add the FilePicker to the page
    page.overlay.append(pick_files_dialog)

    page.go(page.route)

ft.app(target=main)


