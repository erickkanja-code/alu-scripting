#!/usr/bin/python3
"""Documentation to check how many subs for Reddit API. Just to ensure it's well documented"""

import json
import requests

def number_of_subscribers(subreddit):
    headers = {"User-Agent": "desktop:APIactivity:v1.0.0"}
    query = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(query, headers=headers)
    return res.json()["data"]["subscribers"]

if __name__ == "__main__":
    number_of_subscribers("python")
