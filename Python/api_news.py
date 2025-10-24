# Comillas consistentes: Usar comillas dobles para strings

import json
import urllib.request
import urllib.parse

API_KEY = "c9ee89750c8848608c083a26f9fc1e5a"
BASE_URL = "https://newsapi.org/v2/everything"

class NewsSystemError(Exception):
    """Error general en la app"""

    pass


class APIKeyError(NewsSystemError):
    """Error cuando la API KEY es invalida"""

    pass

def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timeout {timeout}"

# def ejemplo_kwargs(**kwargs):
#     pass

print("======")


def newsapi_client(api_key, query, timeout=30, retries=3):
    queiry_string = urllib.parse.urlencode({"q": query, "apiKey": api_key}) 
    url = f"{BASE_URL}?{queiry_string}"
    # print(url)
    try: 
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError:
        print("la API KEY esta vacia")
        return {
            "articles":[]
        }
            
    return f"NewsAPI: {query} con timeout {timeout}"


def fetch_news(api_name, *args, **kwargs):
    """
    Fución flexible para conectar con la API
    """

    base_config = {
        "timeout": 30,
        "retries": 3,
    }

    config = {
        **base_config,
        **kwargs,
    }

    api_clients = {
        "newapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_clients[api_name]
    return client(*args, **config)

response_data = fetch_news("newapi", api_key=API_KEY, query="Python", timeout=10)

for article in response_data["articles"]:
    print(f"- {article['title']}")

response_data = None
try:
    response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
    
except APIKeyError as e:
    print(f"{e}")

if response_data:
    for article in response_data["articles"]:
        print(article["title"])