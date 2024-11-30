import flet as ft
from components.summary import SummaryText


class CustomOverlay(ft.Container):
    def __init__(self, page, title, body, image_src):
        self.page = page
        super().__init__(
            content=self._build(title, body, image_src),
            height=self.page.height,
            width=self.page.width,
            alignment=ft.alignment.center,
            blur=ft.Blur(10, 10, ft.BlurTileMode.CLAMP),
        )

    def _build(
        self,
        title,
        body,
        image_src,
    ):
        news_summary = SummaryText(body)
        return ft.Container(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                ft.Text(
                                    title,
                                    size=18,
                                    color=ft.colors.BLACK,
                                    weight=ft.FontWeight.W_600,
                                ),
                                width=self.page.width * 0.4,
                            ),
                            ft.Container(
                                ft.Image(
                                    image_src,
                                    fit=ft.ImageFit.FILL,
                                ),
                                alignment=ft.alignment.center,
                                height=self.page.height * 0.3,
                                width=self.page.width * 0.4,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Container(
                        ft.Tabs(
                            selected_index=1,
                            tabs=[
                                ft.Tab(
                                    tab_content=ft.Container(ft.Text("summary")),
                                    content=ft.ListView(
                                        [news_summary],
                                        height=self.page.height * 0.35,
                                        width=self.page.width * 0.75,
                                    ),
                                ),
                                ft.Tab(
                                    tab_content=ft.Container(ft.Text("news")),
                                    content=ft.ListView(
                                        [ft.Text(body)],
                                        height=self.page.height * 0.35,
                                        width=self.page.width * 0.75,
                                    ),
                                ),
                            ],
                        ),
                        height=self.page.height * 0.45,
                        width=self.page.width * 0.75,
                    ),
                    ft.Container(
                        ft.ElevatedButton("Close", on_click=self.close_overlay),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            # bgcolor=ft.colors.DEEP_ORANGE_800,
            # padding=ft.padding.all(20),
            # border_radius=10,
            # width=self.page.width * 0.8,
            # height=self.page.height * 0.8,
            # alignment=ft.alignment.center,
        )

    def close_overlay(self, e):
        self.page.overlay.clear()
        self.page.update()
