import flet as ft
from components.appbar import CustomAppbar
from components.newscard import HeadlineCard
from components.overlay import CustomOverlay
from dotenv import load_dotenv
from newsapi.newsgetter import ConfigLoader, NewsFetcher
import json
from llmapi.groq import LlmAPI

news_data = []


def get_news():
    api_key = ConfigLoader.get_api_key()
    news_fetcher = NewsFetcher(api_key)
    news = news_fetcher.fetch_news()
    # news = json.load(open("smaple_data.json", "r"))
    for item in news["top_news"]:
        for news in item["news"]:
            news_data.extend(
                [{"title": news["title"], "body": news["text"], "image": news["image"]}]
            )


def app(page: ft.Page):
    load_dotenv()
    news = get_news()
    page.title = "Daily News"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    appbar = CustomAppbar()
    page.appbar = appbar
    page.add(
        ft.ListView(expand=1, spacing=10),
    )

    def open_overlay(news_index):
        page.overlay.append(
            CustomOverlay(
                page,
                news_data[news_index]["title"],
                news_data[news_index]["body"],
                news_data[news_index]["image"],
            )
        )
        page.update()

    for news in news_data:
        page.controls[0].controls.append(
            HeadlineCard(page, news["title"], news["body"], open_overlay)
        )
        page.update()


ft.app(target=app)
