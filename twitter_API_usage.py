import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
from parse_json import parse_file

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '50'})
    print('Retrieving', url)

    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)['users']
    information = input('What information you want to see about users?'
                        'It can be: name, id, screen_name, friends_count, '
                        'followers_count, time_zone, profile_image_url, '
                        'lang, status, blocking, blocked_by '
                        'location, description, url, crated_at etc. Please '
                        'write ('
                        'divide '
                        'by , ): ').split(',')
    information = [i.strip() for i in information]
    print(parse_file(js, information))
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

