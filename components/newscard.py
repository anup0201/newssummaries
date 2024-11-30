import flet as ft


import flet as ft


class HeadlineCard(ft.Card):
    def __init__(
        self, page: ft.Page, headline: str, body: str, overlay_open_fn
    ) -> None:
        self.page = page
        self.overlay_callback = overlay_open_fn
        super().__init__(
            content=self._build(headline, body),
            # height=self.page.height * 0.15,
            width=self.page.width,
            elevation=10,
            color=ft.colors.BLUE_GREY_200,
        )

    def _build(self, headline: str, body: str) -> ft.Row:
        return ft.Row(
            controls=[
                ft.Container(
                    ft.Column(
                        [
                            ft.Text(
                                headline,
                                color=ft.colors.BLACK,
                                size=16,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                weight=34,
                            ),
                            ft.Text(
                                body,
                                color=ft.colors.BLACK,
                                size=14,
                                max_lines=2,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                        ]
                    ),
                    margin=ft.margin.all(10),
                    expand=1,
                ),
                ft.Container(
                    ft.IconButton(
                        "expand",
                        icon_color=ft.colors.BLACK,
                        bgcolor=ft.colors.DEEP_PURPLE_200,
                        on_click=self._open_overlay,
                    ),
                    margin=ft.margin.all(10),
                ),
            ],
        )

    def _open_overlay(self, e):
        index = self.page.controls[0].controls.index(self)
        self.overlay_callback(index)
