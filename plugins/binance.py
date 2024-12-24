# WARNING: this method only works outside GitHub Actions:
# Binance has restrictions on API access from cloud/datacenter IP ranges.
# To fix this, you'll need to use Binance's API key authentication, even for public endpoints.

# symbol e.g. BTCUSDT
def get_binance_price(symbol: str) -> float:
    """
    Get the current price of a symbol from Binance.
    
    Args:
        symbol (str): Trading pair symbol (e.g., 'BTCUSDT')
    
    Returns:
        float: Current price of the symbol
        
    Raises:
        RequestException: If the API request fails
        KeyError: If the symbol is not found
    """
    import requests
    
    # Binance API endpoint for getting ticker price
    url = f"https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": symbol.upper()}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for non-200 status codes
        data = response.json()
        return float(data["price"])
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch price from Binance: {str(e)}")
    except (KeyError, ValueError) as e:
        raise Exception(f"Invalid symbol or unexpected response format: {str(e)}")

if __name__ == "__main__":
    print(get_binance_price("BTCUSDT"))
