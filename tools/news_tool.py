import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY,
)

prompt = PromptTemplate.from_template("""
You are a financial analyst. Summarize the following financial news headlines about {topic}:

{headlines}

Return a concise summary in plain English.
""")

def summarize_news(topic: str, headlines: list[str]) -> str:
    chain = prompt | llm
    result = chain.invoke({
        "topic": topic,
        "headlines": "\n".join(headlines)
    })
    return result.content.strip() if hasattr(result, "content") else str(result)

