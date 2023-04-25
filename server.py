import requests
import re
import os
from dotenv import load_dotenv

load_dotenv(".env")

URL = os.getenv("URL")
PORT = os.getenv("PORT") if os.getenv("PORT") else 6789


def get_rss_proxy(token):
    req = requests.get(f"https://mikanani.me/RSS/MyBangumi?token={token}")
    return re.sub(r"https://mikanani.me", f"https://{URL}", req.text)


def get_file_proxy(file_path):
    req = requests.get(f"https://mikanani.me/Download/{file_path}")
    return req.content
