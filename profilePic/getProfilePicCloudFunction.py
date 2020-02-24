from tweepy import OAuthHandler
from tweepy import API

def getProfilePic(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()

    if request_json and 'handle' in request_json:
        person = request_json['handle']

        # KEYS
        TWITTER_API_KEY = 'NmKUsZ4A6OLttHgIclyxIlEhV'
        TWITTER_API_SECRET_KEY = '7wYalNckdjwESXa1L0ijMeLHOaLjNQKSt5QuVfqEqJh6m9FUvT'
        TWITTER_ACCESS_TOKEN = '1089278284318142464-SQhuvhyAHkvM8IvYl0Qn5kUrQM6N5r'
        TWITTER_ACCESS_TOKEN_SECRET = 'cKfDtn6qKcmQkOp5CcWWgjNaWNh1TRpwS3T73OSNwH109'

        # INIT
        auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        auth_api = API(auth)

        # GETS THE FINAL DATA
        user = auth_api.get_user(screen_name=person)

        return user.profile_image_url

    else:
        return f'Hello World!'
