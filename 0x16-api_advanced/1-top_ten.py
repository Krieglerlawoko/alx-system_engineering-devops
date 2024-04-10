#!/usr/bin/python3
"""
Hot posts printed on a given Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """Titles of 10 hottest posts printed on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My Reddit Scraper"}  # Set a user agent to avoid being blocked
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title")
            print(title)
    else:
        print("None")
