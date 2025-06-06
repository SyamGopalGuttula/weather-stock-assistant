from tools.news_tool import summarize_news
from langchain_core.runnables import RunnableLambda

# Wrap the news summarization logic in a LangChain agent
def summarize_with_fake_headlines(company: str) -> str:
    headlines = [
        f"{company} stock surges after strong earnings",
        f"{company} partners with AI chipmaker",
        f"Market analysts bullish on {company} for 2025"
    ]
    return summarize_news(company, headlines)

news_agent = RunnableLambda(lambda input: summarize_with_fake_headlines(input))
