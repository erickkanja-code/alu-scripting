#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function to get the number of subscribers from a given subreddit
    """
    headers = {"User-Agent": "desktop:APIactivity:v1.0.0"}
    query = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(query, headers=headers)
    if res.status_code == 200:
        return res.json()["data"]["subscribers"]
    return 0

if __name__ == "__main__":
    number_of_subscribers("python")
