@mcp.tool()
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """
    Convert an amount from one currency to another using current exchange rates.

    Args:
        amount: The amount to convert
        from_currency: Source currency code (e.g., 'USD', 'EUR', 'GBP')
        to_currency: Target currency code (e.g., 'USD', 'EUR', 'GBP')

    Returns:
        A string with the conversion result and exchange rate
    """
    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"
    # Implement try-except to gracefully handle errors
    try:
        # Add a 10-second timeout so the request does not hang
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        rate = data["rates"].get(to_currency)
        if rate is None:
            return f"Could not find exchange rate for {from_currency} to {to_currency}"
        return f"{amount} {from_currency} = {amount * rate:.2f} {to_currency} (Rate: {rate})"
    except requests.exceptions.RequestException as e:
        return f"Error converting currency: {e}"

print(convert_currency(10, "USD", "EUR"))