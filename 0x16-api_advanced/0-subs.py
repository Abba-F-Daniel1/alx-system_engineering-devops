#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom"}

    try:
        # Set allow_redirects=False to prevent following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            try:
                data = response.json()
                return data.get("data", {}).get("subscribers", 0)
            except (ValueError, KeyError):
                return 0
        else:
            return 0
    except requests.RequestException:
        return 0
