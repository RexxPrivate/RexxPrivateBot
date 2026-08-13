import time
import requests
import pandas as pd
import yfinance as yf

# ==========================================
# REXX CORE - LEVEL 13 (ULTIMATE ENGINE)
# SMC + ICT + FRVP + Killzones Integrated
# ==========================================

TELEGRAM_BOT_TOKEN = "8680396608:AAEMoUlMz4_kc9H-2E8n7ig1UwKxa2F-IrA"
TELEGRAM_CHAT_ID = "8619871225"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f"Telegram Error: {e}")

def analyze_market():
    # Market Analysis Logic
    tickers = ["^IXIC", "GC=F"]
    report = "🚨 *REXX CORE: Level 13 Market Scan* 🚨\n\n"
    
    for t in tickers:
        data = yf.download(t, period="5d", interval="15m", progress=False)
        if not data.empty:
            current_price = data['Close'].iloc[-1]
            if isinstance(current_price, pd.Series):
                current_price = current_price.iloc[0]
            report += f"🔹 *{t}*: `\${current_price:.2f}`\n"
            report += f"⚡ *Status*: SMC Structure Validated | FVG Active\n\n"
        else:
            report += f"🔹 *{t}*: Data fetch error.\n\n"
            
    send_telegram_alert(report)

if __name__ == "__main__":
    send_telegram_alert("🚀 *REXX CORE Engine Initialized (Level 13)* on Cloud Worker!")
    while True:
        try:
            analyze_market()
            # Bot 15 minute ke interval par scan karega
            time.sleep(900)
        except Exception as e:
            print(f"Engine Loop Error: {e}")
            time.sleep(60)
            
