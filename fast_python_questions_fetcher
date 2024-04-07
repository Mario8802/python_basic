import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def fetch_python_questions(num_questions=5):
url = "https://api.stackexchange.com/2.2/questions"
params = {
"pagesize": num_questions,
"order": "desc",
"sort": "activity",
"tagged": "python",
"site": "stackoverflow",
}

retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
session = requests.Session()
session.mount('https://', HTTPAdapter(max_retries=retries))

try:
    with session.get(url, params=params) as response:
        response.raise_for_status()
        data = response.json()
        for item in data.get('items', []):
            print("Title:", item.get('title'))
            print("Link:", item.get('link'))
            print("Creation Date:", item.get('creation_date'))
            print("Score:", item.get('score'))
            print("--------------")
except requests.exceptions.RequestException as e:
    print("An error occurred while fetching data:", e)
if name == "main":
num_questions = int(input("Enter the number of Python questions to fetch: "))
fetch_python_questions(num_questions)

