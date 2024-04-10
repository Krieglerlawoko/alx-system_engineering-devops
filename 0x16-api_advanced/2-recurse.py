#!/usr/bin/python3
"""
List of all hot posts querried on a given Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    List of titles of all hot posts
    recursively retrieved on a given subreddit.
    """
    # URL for the subreddit's hot posts constructed in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # headers for the HTTP request defined, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # parameters for the request defined, including pagination and limit
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # GET request sent to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        return None
    # Parse the JSON response and extract relevant data
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    # Append post titles to the hot_list
    for a in results.get("children"):
        hot_list.append(a.get("data").get("title"))

    # If there are more posts to retrieve, recursively call the function
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Return the final list of hot post titles
    return hot_list
