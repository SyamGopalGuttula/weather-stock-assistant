from tools.stock_tool import get_stock_price
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

# Prompt to convert company name to ticker
prompt = PromptTemplate.from_template("""
You are a finance assistant. Convert the company name mentioned in this query to a valid stock ticker symbol.

Examples:
- "Apple stock price" → "AAPL"
- "How is Tesla doing?" → "TSLA"

Query: {query}

Only return the ticker symbol, nothing else.
""")

chain = prompt | llm

# Final agent: first convert, then fetch
stock_agent = RunnableLambda(lambda input: get_stock_price(chain.invoke({"query": input}).content.strip().upper()))
