from tools.stock_tool import get_stock_price
from langchain_core.runnables import RunnableLambda

# Wrap the stock tool as a LangChain-compatible agent
stock_agent = RunnableLambda(lambda input: get_stock_price(input))
