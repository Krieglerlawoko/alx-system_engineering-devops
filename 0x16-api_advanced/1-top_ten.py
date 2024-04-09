import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My Reddit Bot"}  # Set a user agent to avoid rate limiting

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if "data" in data and "children" in data["data"]:
            for post in data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print("None")  # Invalid subreddit or other issue
    except requests.RequestException:
        print("None")  # Error occurred during request
