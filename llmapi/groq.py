import os
from dotenv import load_dotenv
from groq import Groq


class LlmAPI:
    """Singleton class for accessing the Groq API and generating summaries."""

    _instance = None

    def __new__(cls, api_key: str = None):
        if cls._instance is None:
            cls._instance = super(LlmAPI, cls).__new__(cls)
            cls._instance._initialize(api_key)
        return cls._instance

    def _initialize(self, api_key: str = None):
        """Initializes the Groq API instance."""
        api_key = api_key or os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API key not found. Please set API_KEY in .env.")
        self.client = Groq(api_key=api_key)  # Initialize the Groq client

    async def stream_summarize_news(self, news_text: str):
        """Streams a summary using the Groq API.

        Args:
            news_text: The text to summarize.

        Yields:
            Strings representing chunks of the summary as they are generated.
        """
        try:
            completion = self.client.chat.completions.create(
                model="gemma2-9b-it",
                messages=[
                    {
                        "role": "system",
                        "content": "You will receive a news article from user and your task is to summarize the news as accurately as possible in only five bullet points. Make sure the Output is in Markdown format",
                        "role": "user",
                        "content": f"{news_text}",
                    }
                ],
                max_tokens=300,
                top_p=1,
                stream=True,  # Enable streaming
                stop=None,
            )
            for chunk in completion:
                yield chunk.choices[0].delta.content or ""
        except Exception as e:
            yield f"Error summarizing news: {e}"  # Yield the error message to be shown

    def summarize_news(self, news_text):
        try:
            completion = self.client.chat.completions.create(
                model="gemma2-9b-it",  # or any other suitable model
                messages=[
                    {
                        "role": "system",
                        "content": f"""Your task is to summarize the news as accurately as possible in only five bullet points.
                        Don't include any follow up question and don't pretend to have any conversation with any user.
                        The News Artice:{news_text}
                        Summary: """,
                    }
                ],
                max_tokens=300,
                top_p=1,
                stream=False,
                stop=None,
            )
            summary = completion.choices[0].message.content
            return summary
        except Exception as e:
            print(f"Error summarizing news: {e}")
            return ""
