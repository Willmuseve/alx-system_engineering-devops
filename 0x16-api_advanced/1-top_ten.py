#!/usr/bin/python3

"""
A program that queries the reddit Api prints titles of the first 10 hot posts
listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    function that queries Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    Invalid subbredits may return a redirect to serch results
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    usr = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    link = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(link, headers=usr, params=params)
    r = response.json()

    try:
        my_data = r.get('data').get('children')

        for x in my_data:
            print(x.get('data').get('title'))

    except Exception:
        print("None")
