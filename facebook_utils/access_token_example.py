#!/usr/bin/python
# coding: utf-8
import subprocess
from urllib.parse import urlencode, parse_qs

import facebook

# Parameters of your app and the id of the profile you want to mess with.
FACEBOOK_APP_ID = 'XXXXXXXXXXXXXXX'
FACEBOOK_APP_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
FACEBOOK_PROFILE_ID = 'XXXXXX'

# Trying to get an access token. Very awkward.
oauth_args = dict(client_id=FACEBOOK_APP_ID,
                  client_secret=FACEBOOK_APP_SECRET,
                  grant_type='client_credentials')
oauth_curl_cmd = ['curl',
                  'https://graph.facebook.com/oauth/access_token?' + urlencode(oauth_args)]
oauth_response = subprocess.Popen(oauth_curl_cmd,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE).communicate()[0]

try:
    oauth_access_token = parse_qs(str(oauth_response))['access_token'][0]
except KeyError:
    print('Unable to grab an access token!')
    raise

facebook_graph = facebook.GraphAPI(oauth_access_token)

# Try to post something on the wall.
try:
    fb_response = facebook_graph.put_wall_post('Hello from Python', profile_id=FACEBOOK_PROFILE_ID)
    print(fb_response)
except facebook.GraphAPIError as e:
    print('Something went wrong:', e.type, e.message)
