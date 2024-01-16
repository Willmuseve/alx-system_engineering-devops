#!/usr/bin/python3

"""A function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    """

    headers = {"User-Agent": "Karma/0.1"}

    res = requests.get(f"https://api.reddit.com/r/{subreddit}/about.json",
                            headers=headers)

    if res.status_code == 200:
        subreddit_info = res.json()
        return (subreddit_info['data']['subscribers'])
    return 0
