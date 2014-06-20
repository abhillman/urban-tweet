#!/usr/bin/env python
"""
Gets a random page from Urban Dictionary then parses it for
example text. Each example text is checked to see if it is
under 140 characters, so it can be tweeted. Then, the text
is tweeted.
"""
# Python Imports
import re
import sys
import random
import logging

# Library Imports
import twitter
import httplib2
from bs4 import BeautifulSoup

# Tweet Methods
RANDOM_PAGE_URL = 'http://urbandictionary.com/random.php'
MAX_TWEET_LENGTH = 140
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN_KEY = ''
TWITTER_ACCESS_SECRET_TOKEN = ''

def strip_newlines(text):
    """Strips newlines and carriage returns from a piece of text."""
    return re.sub(r'[\r\n]', '', text)

def fetch_conformant_texts():
    """Fetches 'conformant' example texts from an arbitrary page on twitter.
    Conformant example texts are those which are under 140 characters, so
    they can be tweeted."""
    http_handle = httplib2.Http()
    response, content = http_handle.request(RANDOM_PAGE_URL)
    parsed_content = BeautifulSoup(content)
    example_divs = parsed_content.find_all('div', class_='example')
    example_texts = [strip_newlines(div.text) for div in example_divs]
    conformant_texts = filter(lambda text: bool(text) and len(text) < MAX_TWEET_LENGTH, example_texts)
    return conformant_texts

def tweet():
    """Gets a random example text blob from Urban Dictionary and tweets it out."""
    conformant_texts = []
    while not conformant_texts:
        conformant_texts = fetch_conformant_texts()

    chosen_text = random.choice(conformant_texts)

    twitter_api = twitter.Api(
        consumer_key=TWITTER_CONSUMER_KEY,
        consumer_secret=TWITTER_CONSUMER_SECRET,
        access_token_key=TWITTER_ACCESS_TOKEN_KEY,
        access_token_secret=TWITTER_ACCESS_SECRET_TOKEN
    )

    try:
        twitter_api.PostUpdate(chosen_text)
    except twitter.TwitterError,e:
        logging.error(str(e))
        return "Error: %s" % str(e)

    return chosen_text


def main():
    tweet()

if __name__ == '__main__':
    main()
