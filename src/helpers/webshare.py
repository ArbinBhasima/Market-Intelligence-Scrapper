import os
from dotenv import load_dotenv

load_dotenv()

# Webshare Credentials from .env
WEBSHARE_USERNAME = os.getenv("WEBSHARE_USERNAME")
WEBSHARE_PASSWORD = os.getenv("WEBSHARE_PASSWORD")
WEBSHARE_HOST = os.getenv("WEBSHARE_HOST")
WEBSHARE_PORT = os.getenv("WEBSHARE_PORT")


def get_proxy_auth_url():
    """
    Generates the formatted proxy string: http://user:pass@host:port
    """
    auth_str = f"{WEBSHARE_USERNAME}:{WEBSHARE_PASSWORD}"
    return f"http://{auth_str}@{WEBSHARE_HOST}:{WEBSHARE_PORT}"


def get_selenium_wire_options():
    """
    Returns the dictionary required by selenium-wire to handle authentication.
    Replaces your old get_sbr_connection() logic.
    """
    proxy_url = get_proxy_auth_url()

    return {
        "proxy": {
            "http": proxy_url,
            "https": proxy_url,
            "no_proxy": "localhost,127.0.0.1",
        }
    }
