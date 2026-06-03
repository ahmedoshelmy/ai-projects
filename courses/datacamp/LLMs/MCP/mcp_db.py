# Add lookup_currencies(prefix): find rows where name or code contains prefix
@mcp.tool()
def lookup_currencies(prefix: str) -> str:
    """Find currencies whose code or name contains the given prefix."""
    try:
        # Use parameterized query and LIMIT 50
        cursor = conn.execute(
            "SELECT code, name FROM currencies WHERE name LIKE ? OR code LIKE ? LIMIT 50",
            (f"%{prefix}%", f"%{prefix}%")
        )
        rows = cursor.fetchall()
        return "\n".join(f"{row['code']} - {row['name']}" for row in rows)
    except sqlite3.Error as e:
        return f"Database error: {e}"

print(lookup_currencies("Euro"))


@mcp.tool()
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """Convert an amount from one currency to another using current exchange rates."""
    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"
    # Read optional API key from the server's environment
    headers = {}
    api_key = os.environ.get("CURRENCY_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    try:
        # Pass headers (and timeout) to the request; key never goes in the URL
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        rate = data["rates"].get(to_currency)
        if rate is None:
            return f"Could not find exchange rate for {from_currency} to {to_currency}"
        return f"{amount} {from_currency} = {amount * rate:.2f} {to_currency} (Rate: {rate})"
    except requests.exceptions.RequestException as e:
        return f"Error converting currency: {e}"

print(convert_currency(10, "USD", "EUR"))