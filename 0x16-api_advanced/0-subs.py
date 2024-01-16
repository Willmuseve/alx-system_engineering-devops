#!/usr/bin/python3

"""A function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for an existing
    subreddit
    Return:
        number of subscribers (int)
    """
    link = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Chrome/88.0.4324.188'}

    response = requests.get(link, headers=header)

    if not response:
        return 0
    else:
        data = response.json().get('data')
        return data.get('subscribers')
