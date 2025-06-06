import requests

def get_stock_price(symbol: str) -> str:
    try:
        symbol = symbol.upper().strip()
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=1d&interval=1d"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return f"Error: Unable to fetch data for '{symbol}' (status code {response.status_code})"

        data = response.json()
        result = data["chart"]["result"]

        if not result:
            return f"No stock data found for '{symbol}'"

        meta = result[0]["meta"]
        price = meta.get("regularMarketPrice")

        if price is None:
            return f"No price data available for '{symbol}'"

        return f"The current price of {symbol} is ${price:.2f}."

    except Exception as e:
        return f"Error fetching stock price: {str(e)}"
