from tools.news_tool import summarize_news
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

# Prompt to extract company name
prompt = PromptTemplate.from_template("""
Extract the company name or stock name mentioned in the user query.

Query: {query}

Only return the company name. If you can't find one, return "Unknown".
""")

extract_chain = prompt | llm

def news_agent_logic(user_query: str) -> str:
    company = extract_chain.invoke({"query": user_query}).content.strip().title()
    if company.lower() == "unknown":
        return "Sorry, I couldn't identify the company you're asking about."

    # Simulated headlines for now
    headlines = [
        f"{company} stock rises after strong earnings",
        f"{company} announces new AI product",
        f"Analysts upgrade {company} to 'Buy'"
    ]

    summary = summarize_news(company, headlines)
    return summary.content.strip() if hasattr(summary, "content") else summary

news_agent = RunnableLambda(news_agent_logic)
