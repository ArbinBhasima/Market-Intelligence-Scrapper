# import os
# from dotenv import load_dotenv
# from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

# load_dotenv()

# BRIGHT_DATA_USERNAME = os.getenv("BRIGHT_DATA_USERNAME")
# BRIGHT_DATA_PASSWORD = os.getenv("BRIGHT_DATA_PASSWORD")
# BRIGHT_DATA_HOST = os.getenv("BRIGHT_DATA_HOST", "brd.superproxy.io")

# BRIGHT_DATA_DEFAULT_PORT = 9222
# BRIGHT_DATA_SELENIUM_PORT = 9515


# def get_proxy_url(use_selenium=False):
#     port = BRIGHT_DATA_SELENIUM_PORT if use_selenium else BRIGHT_DATA_DEFAULT_PORT
#     auth_str = f"{BRIGHT_DATA_USERNAME}:{BRIGHT_DATA_PASSWORD}"
#     return f"https://{auth_str}@{BRIGHT_DATA_HOST}:{port}"


# def get_sbr_connection():
#     proxy_url = get_proxy_url(use_selenium=True)
#     return ChromiumRemoteConnection(proxy_url, "goog", "chrome")
