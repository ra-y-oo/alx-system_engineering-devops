#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[]):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User Agent': 'MyAPI/0.01'}

    # URL to query the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            # Extract the list of posts from the JSON response
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            # Check if there are more pages of results (pagination)
            after = data['data']['after']
            if after:
                # Recursively call the function with the next page
                return recurse(subreddit, hot_list=hot_list)
            else:
                return hot_list
        elif response.status_code == 404:
            # Subreddit not found, return None
            return None
        else:
            # Other error, handle as needed
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    