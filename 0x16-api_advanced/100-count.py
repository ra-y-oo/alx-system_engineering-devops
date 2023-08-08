#!/usr/bin/python3
import requests
from collections import Counter

def count_words(subreddit, word_list, after=None, word_counter=None):
    if word_counter is None:
        word_counter = Counter()

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User Agent': 'MyAPI/0.01'}

    # URL to query the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'

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
                lowercase_title = title.lower()

                # Count occurrences of words from word_list
                for word in word_list:
                    if word in lowercase_title:
                        word_counter[word] += lowercase_title.count(word)

            # Check if there are more pages of results (pagination)
            after = data['data']['after']
            if after:
                # Recursively call the function with the next page
                return count_words(subreddit, word_list, after=after, word_counter=word_counter)
            else:
                # Print sorted word count results
                sorted_results = sorted(word_counter.items(), key=lambda item: (-item[1], item[0]))
                for word, count in sorted_results:
                    print(f"{word}: {count}")
                return
        elif response.status_code == 404:
            # Subreddit not found, print nothing
            return
        else:
            # Other error, handle as needed
            print(f"Error: {response.status_code} - {response.text}")
            return
    except Exception as e:
        print(f"Error: {e}")
        return
    