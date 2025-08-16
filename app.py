import streamlit as st
import pandas as pd
import requests
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# --- Page Config ---
st.set_page_config(page_title="Crypto Dashboard", page_icon="🪙", layout="wide")

# --- Auto Refresh every 60 sec ---
st_autorefresh(interval=60 * 1000, key="crypto_refresh")

# --- Custom CSS for blinking dot ---
st.markdown("""
<style>
.blink {
  animation: blinker 1.2s linear infinite;
  font-weight: bold;
  color: limegreen;
}
@keyframes blinker {
  50% { opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# --- Title with Blinking Live Dot ---
st.markdown("## 📊 Top 10 Cryptocurrencies by Market Cap <span class='blink'>🟢 LIVE</span>", unsafe_allow_html=True)

# --- Show Live Timestamp ---
last_updated = datetime.now().strftime("%I:%M:%S %p")
st.caption(f"⏱ Last updated: {last_updated} (auto-refreshes every 60s)")

# --- Fetch Data from CoinGecko ---
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}
response = requests.get(url, params=params)
data = response.json()

# --- Build DataFrame ---
df = pd.DataFrame(data, columns=[
    "market_cap_rank", "image", "name", "symbol", 
    "current_price", "price_change_percentage_24h", 
    "price_change_24h", "total_volume", "market_cap"
])

# --- Helper to format with colors ---
def color_text(value, is_percent=False):
    if value is None:
        return "-"
    if value >= 0:
        color = "green"; symbol = "▲"
    else:
        color = "red"; symbol = "▼"
    if is_percent:
        return f"<span style='color:{color}'>{symbol} {value:.2f}%</span>"
    else:
        return f"<span style='color:{color}'>{symbol} ${value:,.2f}</span>"

# --- Format large numbers like 500M, 4.5T ---
def human_format(num):
    for unit in ["", "K", "M", "B", "T"]:
        if abs(num) < 1000.0:
            return f"{num:3.1f}{unit}"
        num /= 1000.0
    return f"{num:.1f}P"

# --- Build Styled Data ---
rows = []
for _, row in df.iterrows():
    rows.append([
        row["market_cap_rank"],
        f"<img src='{row['image']}' width='20'> {row['name']} ({row['symbol'].upper()})",
        f"${row['current_price']:,.2f}",
        color_text(row["price_change_percentage_24h"], is_percent=True),
        color_text(row["price_change_24h"]),
        f"${human_format(row['total_volume'])}",
        f"${human_format(row['market_cap'])}"
    ])

styled_df = pd.DataFrame(rows, columns=[
    "#", "Cryptocurrency", "Price (USD)", "24h %", "24h Change", "24h Volume", "Market Cap"
])

# --- Show Table with HTML ---
st.write(
    styled_df.to_html(escape=False, index=False),
    unsafe_allow_html=True
)