from tools.news_tool import summarize_news
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

# Prompt to extract topic
prompt = PromptTemplate.from_template("""
Extract the main topic of interest from the user's query. This could be a company, country, sector, or keyword.

Query: {query}

Return only the topic name. If you can't find any, return "Unknown".
""")


extract_chain = prompt | llm

def news_agent_logic(user_query: str) -> str:
    topic = extract_chain.invoke({"query": user_query}).content.strip().title()
    if topic.lower() == "unknown":
        return "Sorry, I couldn't identify the topic you're asking about."

    headlines = [
        f"{topic} sees global attention amid market shifts",
        f"Experts weigh in on recent developments in {topic}",
        f"{topic} becomes focus in latest economic report"
    ]

    return summarize_news(topic, headlines)

news_agent = RunnableLambda(news_agent_logic)
