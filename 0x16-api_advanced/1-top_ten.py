import requests

def top_ten(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User Agent': 'MyAPI/0.01'}

    # URL to query the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

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
                print(title)
        elif response.status_code == 404:
            # Subreddit not found, print None
            print("None")
        else:
            # Other error, handle as needed
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error: {e}")
