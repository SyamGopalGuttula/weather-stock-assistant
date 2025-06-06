from tools.weather_tool import get_weather
from langchain_core.runnables import RunnableLambda

# Wrap the weather tool as a LangChain-compatible "agent"
weather_agent = RunnableLambda(lambda input: get_weather(input))
