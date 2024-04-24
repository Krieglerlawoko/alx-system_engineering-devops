#!/usr/bin/python3
"""
Hot posts on a given Reddit subreddit printed
"""

import requests


def top_ten(subreddit):
    """Titles of the 10 hottest posts on a given subreddit printed"""
    # URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # headers for the HTTP request defined, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Parameters for the request defined, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    # GET request sent to subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Response status code indicates a not-found error (404)
    if response.status_code == 404:
        print("None")
        return

    # JSON response parsed and extract the 'data' section
    results = response.json().get("data")

    # Titles of the top 10 hottest posts printed
    [print(c.get("data").get("title")) for c in results.get("children")]
