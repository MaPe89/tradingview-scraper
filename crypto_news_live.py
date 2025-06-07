import time
from tradingview_scraper.symbols.news import NewsScraper

TOP_10_CRYPTOS = [
    ("BTCUSDT", "BINANCE"),
    ("ETHUSDT", "BINANCE"),
    ("BNBUSDT", "BINANCE"),
    ("SOLUSDT", "BINANCE"),
    ("XRPUSDT", "BINANCE"),
    ("ADAUSDT", "BINANCE"),
    ("DOGEUSDT", "BINANCE"),
    ("TONUSDT", "BINANCE"),
    ("AVAXUSDT", "BINANCE"),
    ("TRXUSDT", "BINANCE"),
]


def main():
    scraper = NewsScraper()
    seen = {symbol: set() for symbol, _ in TOP_10_CRYPTOS}
    while True:
        for symbol, exchange in TOP_10_CRYPTOS:
            try:
                headlines = scraper.scrape_headlines(symbol=symbol, exchange=exchange, sort="latest")
            except Exception as exc:
                print(f"Error fetching news for {symbol}: {exc}")
                continue
            for item in headlines:
                news_id = item.get("id")
                if news_id and news_id not in seen[symbol]:
                    seen[symbol].add(news_id)
                    published = item.get("published_datetime", item.get("published"))
                    title = item.get("title")
                    print(f"{symbol} | {published} | {title}")
        time.sleep(300)


if __name__ == "__main__":
    main()
