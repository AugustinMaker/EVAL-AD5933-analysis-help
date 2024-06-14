
from conversion import conversion
from mosaique import standard_mosaique
import flet as ft
from flet import Page, View, AppBar, Text, ElevatedButton, TextField, colors, Column, Image

def main(page: Page):
    print("Initial route:", page.route)
    history_stack = []

    analysis_name_input = ft.TextField(label="Analysis name")
    result_column = ft.Ref[Column]()

    def pick_files_result_format(e: ft.FilePickerResultEvent):
        file_paths = [f.path for f in e.files]
        selected_files.value = (
            ", ".join([f.name for f in e.files]) if e.files else "Cancelled!"
        )
        selected_files.update()
        conversion(file_paths)  # Appel de la fonction conversion avec les fichiers sélectionnés

    def pick_files_result_standard(e: ft.FilePickerResultEvent):
        file_paths = [f.path for f in e.files]
        selected_files.value = (
            ", ".join([f.name for f in e.files]) if e.files else "Cancelled!"
        )
        selected_files.update()


    pick_files_dialog_format = ft.FilePicker(on_result=pick_files_result_format)
    pick_files_dialog_standard = ft.FilePicker(on_result=pick_files_result_standard)
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
                    ElevatedButton("Plot graph", on_click=open_plot_graph),
                    ElevatedButton("Peak analysis", on_click=open_settings)
                ])
            )
        elif page.route == "/format":
            page.views.append(
                View("/format", [
                    create_app_bar("Format"),
                    Text("Format Files", style="bodyMedium"),
                    ElevatedButton(
                        "Pick files",
                        icon=ft.icons.UPLOAD_FILE,
                        on_click=lambda _: pick_files_dialog_format.pick_files(allow_multiple=True)
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
        elif page.route == "/plot_graph":
            page.views.append(
                View("/plot_graph", [
                    create_app_bar("Plot Graph"),
                    ElevatedButton("Standard analysis", on_click=open_standard_analysis),
                    ElevatedButton("Specific analysis", on_click=open_specific_analysis),
                    ElevatedButton("Temporal evolution", on_click=open_temporal_evolution)
                ])
            )
        elif page.route == "/standard_analysis":
            page.views.append(
                View("/standard_analysis", [
                    create_app_bar("Standard Analysis"),
                    Text("Select files"),
                    ElevatedButton(
                        "Pick files",
                        icon=ft.icons.UPLOAD_FILE,
                        on_click=lambda _: pick_files_dialog_standard.pick_files(allow_multiple=True)
                    ),
                    analysis_name_input,
                    ElevatedButton("Start", on_click=start_standard_analysis),
                    selected_files
                ])
            )
        elif page.route == "/specific_analysis":
            page.views.append(
                View("/specific_analysis", [
                    create_app_bar("Specific Analysis"),
                    Text("Specific Analysis page!")
                ])
            )
        elif page.route == "/temporal_evolution":
            page.views.append(
                View("/temporal_evolution", [
                    create_app_bar("Temporal Evolution"),
                    Text("Temporal Evolution page!")
                ])
            )
        elif page.route == "/standard_analysis/result":
            page.views.append(
                View("/standard_analysis/result", [
                    create_app_bar("Analysis Result"),
                    ft.Image(
                        src=f"/output/bernielo/bernieloFI.png",
                        width=100,
                        height=100,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Row(expand=1, wrap=False, scroll="always")
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

    def open_plot_graph(e):
        history_stack.append(page.route)
        page.go("/plot_graph")

    def open_standard_analysis(e):
        history_stack.append(page.route)
        page.go("/standard_analysis")

    def open_specific_analysis(e):
        history_stack.append(page.route)
        page.go("/specific_analysis")

    def open_temporal_evolution(e):
        history_stack.append(page.route)
        page.go("/temporal_evolution")

    def start_standard_analysis(e):
        analysis_name = analysis_name_input.value.strip()
        if not analysis_name:
            print("Veuillez entrer un nom d'analyse valide.")
            return

        selected_filenames = selected_files.value.split(", ")
        if not selected_filenames or selected_filenames[0] == "Cancelled!":
            print("Veuillez sélectionner des fichiers.")
            return

        # Appel de la fonction standard_mosaique
        image_files = standard_mosaique(selected_filenames, analysis_name)

        # Mise à jour de la colonne des résultats
        if result_column.current:
            result_column.current.controls.clear()
            for image_file in image_files:
                result_column.current.controls.append(Image(src=f"/path/to/your/images/{image_file}"))
            result_column.current.update()

        # Naviguer vers la page de résultats
        history_stack.append(page.route)
        page.go("/standard_analysis/result")

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Add the FilePicker to the page
    page.overlay.append(pick_files_dialog_format)
    page.overlay.append(pick_files_dialog_standard)

    page.go(page.route)

ft.app(target=main)
