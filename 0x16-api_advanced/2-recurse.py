#!/usr/bin/python3
"""
 a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """func itself """

    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    link = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    results = requests.get(link, params=params, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for x in all_titles:
            hot_list.append(x.get("data").get("title"))
        return hot_list
    else:
        return (None)
