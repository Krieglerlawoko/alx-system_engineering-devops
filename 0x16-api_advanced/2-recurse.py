import requests

def recurse(subreddit, hot_list=[]):
    """
    Reddit API recursively queried to retrieve hot article titles for a given subreddit.
    """
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit API Client"}

    try:
        response = requests.get(base_url, headers=headers)
        response_data = response.json()

        if "data" in response_data and "children" in response_data["data"]:
            articles = response_data["data"]["children"]
            for article in articles:
                title = article["data"]["title"]
                hot_list.append(title)

            if "after" in response_data["data"]:
                after = response_data["data"]["after"]
                return recurse(subreddit, hot_list=hot_list)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
