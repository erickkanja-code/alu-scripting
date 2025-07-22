#!/usr/bin/python3
"""
Function querrying the Reddit API and prints the titles of the first 10 hot posts listed for a subreddit
"""

import json
import requests

def top_ten(subreddit):
    headers = {"User-Agent": "desktop:TopTenActivity:v1.0.0"}
    query = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": "10"}
    res = requests.get(query, headers=headers, params=params)
    if (res.status_code == 200):
        i = 0
        while (i < 10):
            print(res.json()['data']['children'][i]['data']['title'])
            i += 1
    else:
            return 0

if __name__ == "__main__":
    top_ten("python")
