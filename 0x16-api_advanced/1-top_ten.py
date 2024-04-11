#!/usr/bin/python3
"""
Hot posts printed on a given Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """Titles of 10 hottest posts printed on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors

        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("None")
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            print("None")
        else:
            print(f"Error: {e}")
