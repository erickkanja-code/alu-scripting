#!/usr/bin/python3
"""
Module: 2-recurse.py
Purpose: Recursive function that returns a list containing titles of all hot articles for a fiven subreddit
"""
import json
import requests

def recurse(subreddit, hot_list=[], after=None):
    query = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"USER-AGENT": "laptop:Assignment2Script2:v1.1.0"}
    params = {"after": after}
    response = requests.get(query, headers=headers, params=params)
    children = response.json()['data']['children']
    for child in children:
        title = child['data']['title']
        hot_list.append(title)

    after = response.json()['data']['after']
    if after:
        recurse(subreddit, hot_list, after)
    else:
        return hot_list

if __name__ == "__main__":
    recurse("csmajors")
