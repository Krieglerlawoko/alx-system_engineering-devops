#!/usr/bin/python3
"""
Words in all hot posts of a given Reddit subreddit counted.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Reddit API queried, parses the titles
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    children = data["data"]["children"]

    for p in children:
        title = p["data"]["title"].lower()
        for w in word_list:
            if w.lower() in title:
                counts[w] = counts.get(w, 0) + title.count(w.lower())

    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
