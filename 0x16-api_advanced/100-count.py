#!/usr/bin/python3
"""Advanced API module using reddit api endpoint"""
from operator import itemgetter
import requests


def recurse(subreddit, top_list=[]):
    """Return list of title of the top posts in a subreddit."""
    def recurse_post(lst, post_list, curr_idx):
        """Recursively add all title to top_list."""
        if curr_idx >= len(post_list):
            return
        title = post_list[curr_idx]['data']['title']
        lst.append(title)
        recurse_post(lst, post_list, curr_idx + 1)

    def get_post(limit, after, url, header, post_list):
        """Recursively make request to reddit api(Handled its pagination)."""
        if limit >= len(post_list):
            return
        url = '{}&after={}'.format(url, after)
        response = requests.get(url, headers=header)
        result = response.json()['data']
        post_list = result['children']
        after = result['after']
        recurse_post(top_list, post_list, 0)
        get_post(limit, after, url, header, post_list)

    header = {
            'User-Agent': 'MyBot/1.0'
            }
    limit = 100
    url = 'https://reddit.com/r/{}/top.json?limit={}'.format(subreddit, limit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        result = response.json()['data']
        post_list = result['children']
        after = result['after']
        recurse_post(top_list, post_list, 0)
        get_post(limit, after, url, header, post_list)
        return top_list
    else:
        return None


def count_words(subreddit, words_list):
    """Print stats of word_list in the hot topics in a subreddit."""
    def count_word(word, title, t_curr_idx, count=0):
        """Return the number appear of word in title."""
        if t_curr_idx >= len(title):
            return count
        if word == title[t_curr_idx]:
            count += 1
        return count_word(word, title, t_curr_idx + 1, count)

    def get_stats(word_list, w_curr_idx, title_list, t_curr_idx, stats):
        """Recursively get the stats."""
        if t_curr_idx == len(title_list) - 1:
            t_curr_idx = 0
            w_curr_idx += 1
        if w_curr_idx >= len(word_list):
            return

        word = word_list[w_curr_idx].lower()
        title = title_list[t_curr_idx].lower()
        count = count_word(word, title.split(), 0)
        stats[word] = count + stats.get(word, 0)
        get_stats(word_list, w_curr_idx, title_list, t_curr_idx + 1, stats)

    def print_stats(stats, curr_idx):
        """Recursively print the stats."""
        if curr_idx >= len(stats):
            return
        k, v = stats[curr_idx]
        if v > 0:
            print('{}: {}'.format(k, v))
        print_stats(stats, curr_idx + 1)

    stats = {}
    title_list = recurse(subreddit)
    if not title_list:
        return
    get_stats(words_list, 0, title_list, 0, stats)
    stats = sorted(stats.items(), key=lambda k: (
        k[1], itemgetter(0)(k)), reverse=True)
    print_stats(stats, 0)
