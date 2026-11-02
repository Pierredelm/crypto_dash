import requests


def get_usd_exchange_rate() -> float:
    """Fetches the live EUR to USD exchange rate from an external API."""
    response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR", timeout=5)
    response.raise_for_status()
    data = response.json()
    return data["rates"]["USD"]

def process_payment_in_usd(amount_eur: float) -> float:
    """Converts EUR amount to USD using the live exchange rate."""
    rate = get_usd_exchange_rate()
    return round(amount_eur * rate, 2)
