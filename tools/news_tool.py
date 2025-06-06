import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Google API key is missing from .env")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY,
)

prompt = PromptTemplate.from_template("""
You are a financial analyst. Summarize the following financial news headlines about {company}:

{headlines}

Return a concise summary in plain English.
""")

def summarize_news(company: str, headlines: list[str]) -> str:
    chain = prompt | llm
    input_text = {
        "company": company,
        "headlines": "\n".join(headlines)
    }
    return chain.invoke(input_text)
