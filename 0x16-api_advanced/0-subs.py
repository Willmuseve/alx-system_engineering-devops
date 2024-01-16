#!/usr/bin/python3

"""A function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers
    """
    link = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Chrome/88.0.4324.188'}

    r = requests.get(link, headers=header)

    if not r:
        return 0
    else:
        x = r.json().get('data')
        return x.get('subscribers')
