if __name__ == '__main__':
    # graph = facebook.GraphAPI(APP_ACCESS_TOKEN)
    # access_token = graph.get_app_access_token(APP_ID, APP_SECRET)
    # print(access_token)
    # graph.access_token = access_token
    # oauth_args = dict(client_id=APP_ID,
    #                   client_secret=APP_SECRET,
    #                   grant_type='client_credentials')
    # result = graph.request(path='oauth/access_token', args=oauth_args)
    # print(result)
    #
    # fb_response = graph.put_wall_post('Hello from Python', profile_id='100010757350414')
    # print(fb_response)

    scope = ['publish_stream', 'user_photos', 'user_status']
    url = 'https://www.facebook.com/dialog/oauth'
    qs = {
        'client_id': APP_ID,
        'client_secret': APP_SECRET,
        'redirect_uri': self.redirect_uri,
        'display': display,
        'scope': ','.join(scope)
    }
    print('%s?%s' % (url, urlencode(qs)))

