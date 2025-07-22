#!/usr/bin/python3
"""
Module: 1-top_ten.py
Purpose: Print titles of first 10 hot posts in a subreddit
"""



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
    import json
    import requests
    top_ten("python")
