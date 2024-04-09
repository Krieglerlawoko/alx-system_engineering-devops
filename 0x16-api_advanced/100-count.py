import requests

def count_words(subreddit, word_list):
    def get_hot_articles(subreddit, after=None):
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        params = {"limit": 100, "after": after}
        headers = {"User-Agent": "Reddit Keyword Counter"}

        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if "data" in data and "children" in data["data"]:
            articles = data["data"]["children"]
            return articles, data["data"]["after"]
        else:
            return [], None

    def parse_title(title, word_list):
        title_lower = title.lower()
        for w in word_list:
            if w.lower() in title_lower:
                return w
        return None

    def count_keywords(articles, word_list, counts):
        for article in articles:
            title = article["data"]["title"]
            keyword = parse_title(title, word_list)
            if keyword:
                counts[keyword] = counts.get(keyword, 0) + 1

        return counts

    def print_sorted_counts(counts):
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")

    def recursive_query(subreddit, word_list, after=None, counts=None):
        if counts is None:
            counts = {}

        articles, next_after = get_hot_articles(subreddit, after)
        counts = count_keywords(articles, word_list, counts)

        if next_after:
            recursive_query(subreddit, word_list, next_after, counts)
        else:
            print_sorted_counts(counts)

    recursive_query(subreddit, word_list)
