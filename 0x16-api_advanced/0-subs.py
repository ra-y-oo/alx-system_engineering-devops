#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent
    headers = {'User Agent': 'MyAPI/0.01'}

    # URL to query the subreddit's information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            # Extract the number of subscribers from the JSON response
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            # Subreddit not found, return 0
            return 0
        else:
            # Other error, handle as needed
            print(f"Error: {response.status_code} - {response.text}")
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0
