import flet as ft


class CustomAppbar(ft.AppBar):
    def __init__(self):
        super().__init__(
            title=ft.Text("Daily News", color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE_GREY_900,
            center_title=True,
        )
