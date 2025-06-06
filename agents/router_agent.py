import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

prompt = PromptTemplate.from_template("""
You are a routing assistant. Your job is to decide which type of query this is:

- If it's asking about current weather, return "weather"
- If it's asking about a stock or ticker symbol, return "stock"
- If it's asking for news, headlines, or summaries, return "news"

User query: {input}

Only return one word: "weather", "stock", or "news".
""")

router_chain = prompt | llm

router_agent = RunnableLambda(
    lambda input: router_chain.invoke({"input": input}).content.strip().lower()
)

