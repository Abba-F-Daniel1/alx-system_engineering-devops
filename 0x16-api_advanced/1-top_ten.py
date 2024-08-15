#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}

    try:
        # Set allow_redirects=False to prevent following redirects
        response = requests.get(url, headers=headers, allow_redirects=False, params={"limit": 10})

        if response.status_code == 200:
            try:
                data = response.json()
                posts = data.get("data", {}).get("children", [])
                if not posts:
                    print(None)
                    return
                
                for post in posts:
                    title = post.get("data", {}).get("title")
                    if title:
                        print(title)
            except (ValueError, KeyError):
                print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)
