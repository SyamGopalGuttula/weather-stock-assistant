from tools.weather_tool import get_weather
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Gemini LLM setup
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

# Prompt to extract city name
prompt = PromptTemplate.from_template("""
You are a helpful assistant. From the following user query, extract only the city name relevant to the weather question.

Query: {query}

Return only the city name. If no city is mentioned, say "Unknown".
""")

chain = prompt | llm

# Use Gemini to extract city name, then call weather tool
def get_weather_via_llm(input: str) -> str:
    city = chain.invoke({"query": input}).content.strip().title()
    if city.lower() == "unknown":
        return "Sorry, I couldn't find the city in your question."
    return get_weather(city)

weather_agent = RunnableLambda(get_weather_via_llm)
