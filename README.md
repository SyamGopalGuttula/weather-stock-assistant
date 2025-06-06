# LangGraph Multi-Agent Assistant

A command-line assistant powered by **LangGraph**, **LangChain**, and **Google Gemini**, capable of:

- Answering weather queries (via OpenWeatherMap)
- Getting live stock prices (via yfinance)
- Summarizing financial news and general topics (via Gemini)
- Smart routing using an LLM-based router agent
- Answering general knowledge questions (via Gemini)
- Flow control using LangGraph

---

## Features

- LLM-powered company/topic/city extraction
- Multi-agent routing via LangGraph
- Supports general questions using Gemini
- Modular, testable structure
- Built for future UI and RAG integrations

---

## Tech Stack

- [`LangGraph`](https://github.com/langchain-ai/langgraph)
- [`LangChain`](https://github.com/langchain-ai/langchain)
- [`Google Generative AI`](https://ai.google.dev/) via `langchain-google-genai`
- [`yfinance`](https://pypi.org/project/yfinance/) for live stock prices
- [`OpenWeatherMap API`](https://openweathermap.org/current)
- Python 3.11 recommended

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/weather-stock-assistant.git
cd weather-stock-assistant
```

### 2. Create virtual environment

```bash
# On Windows
py -3.11 -m venv venv
.venv\Scripts/Activate

# On Mac/Linux
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## API Keys Setup

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_key
OPENWEATHER_API_KEY=your_openweathermap_key
```

- Get your Gemini API key from **[Google AI Studio](https://makersuite.google.com/app/apikey)** (previously MakerSuite)
- Get a free API key at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)

---

## How to Run

```bash
python main.py
```

You'll see:

```
Welcome to the LangGraph Multi-Agent Assistant!
Type 'exit' to quit.
```

Try queries like:

- `What's the weather in Delhi?`
- `Show me Amazon stock price`
- `Give me news about Elon Musk`
- `What's happening in AI?`
- `Who is the CEO of Tesla?`
- `Tell me a joke`

---

## Project Structure

```
weather-stock-assistant/
├── agents/
│   ├── weather_agent.py
│   ├── stock_agent.py
│   ├── news_agent.py
│   ├── general_agent.py
│   └── router_agent.py
├── tools/
│   ├── weather_tool.py
│   ├── stock_tool.py
│   └── news_tool.py
├── langgraph_app/
│   └── graph.py
├── main.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
```

---

## How It Works

- The `router_agent` uses Gemini to classify intent:
  - "weather", "stock", "news", or "general"
- LangGraph routes the query to the appropriate agent
- Each agent:
  - Uses Gemini to extract or interpret input
  - Calls its tool (e.g., weather API, yfinance)
- General agent answers open-ended queries via Gemini

---

## Future Plans

- Add a Streamlit UI
- Pull real news via RSS or Google News APIs
- Analyze how weather patterns affect stock prices
- Extend LangGraph flow with memory or RAG

---

## Credits

Built with:
- LangChain + LangGraph
- Google Gemini (via AI Studio)
- OpenWeatherMap + Yahoo Finance APIs