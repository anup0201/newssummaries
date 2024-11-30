import os
from datetime import datetime, timezone, date
import requests


class ConfigLoader:
    @staticmethod
    def get_api_key() -> str:
        api_key = os.getenv("NEWS_API_KEY")
        return api_key


class URLBuilder:
    @staticmethod
    def build_url(
        news_date: date,
        country_code,
        language,
    ):
        base_url = "https://api.worldnewsapi.com/top-news"
        foramtted_date = news_date.strftime("%Y-%m-%d")
        return f"{base_url}?source-country={country_code}&language={language}&date={foramtted_date}"


class NewsFetcher:
    def __init__(
        self, api_key: str, country_code: str = "in", language: str = "en"
    ) -> None:
        self.api_key = api_key
        self.country_code = country_code
        self.language = language

    def fetch_news(self, news_date: date = datetime.now(timezone.utc).date()):
        url = URLBuilder.build_url(news_date, self.country_code, self.language)
        headers = {"x-api-key": self.api_key}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(e)
            return {}
