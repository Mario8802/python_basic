stack exchange api

import requests

def fetch_python_questions():
    url = "https://api.stackexchange.com/2.2/questions"
    params = {
        "pagesize": 5,  # Number of questions to fetch
        "order": "desc",
        "sort": "activity",
        "tagged": "python",  # Questions tagged with 'python'
        "site": "stackoverflow",
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            for item in data['items']:
                print("Title:", item['title'])
                print("Link:", item['link'])
                print("Creation Date:", item['creation_date'])
                print("Score:", item['score'])
                print("--------------")
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    fetch_python_questions()
