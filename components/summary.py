import flet as ft
from llmapi import groq


class SummaryText(ft.Markdown):
    def __init__(self, body):
        super().__init__()
        self.body = body
        self.value = ""

    def did_mount(self):
        self.page.run_task(self.stream_summary)

    async def stream_summary(self):
        llm_api = groq.LlmAPI()
        async for chunk in llm_api.stream_summarize_news(self.body):
            self.value += chunk
            self.update()

    async def summarize(self):
        llm_api = groq.LlmAPI()
        self.value = llm_api.summarize_news(self.body)
        self.update()
