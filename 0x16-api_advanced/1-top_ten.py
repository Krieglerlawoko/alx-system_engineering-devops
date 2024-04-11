#!/usr/bin/python3
'''
    function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
<<<<<<< HEAD
        top ten posts for a given subreddit returned
=======
        Top ten posts for a given subreddit returned
>>>>>>> baa1378ce6c8256767cedef98f885500f6eef291
    '''
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
