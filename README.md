Gets a random page from Urban Dictionary then parses it for
example text. Each example text is checked to see if it is
under 140 characters, so it can be tweeted. Then, the text
is tweeted.

Be sure to enter consumer consumer and access keys and
secrets before use.

Example: https://twitter.com/Horse_ebookz

Dependencies are:
- httplib2 for downloading from Urban Dictionary
- bs4 (aka BeautifulSoup) for parsing HTML documents from Urban Dictionary
- twitter (i.e. python-twitter) for posting to twitter

Aryeh Hillman (c) 2014
