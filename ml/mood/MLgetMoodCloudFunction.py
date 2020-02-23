'''ml1 layer - tweets setement value'''

from google.cloud import language
from io import StringIO
import pandas as pd

def MLgetMood(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()

    if request_json and 'tweets' in request_json:
        tweets = StringIO(request_json['tweets'])

        client = language.LanguageServiceClient()
        twitterProfile = pd.read_csv(tweets, sep=',', header=None)
        profileSentiment = []
        count = 0
        for tweet in twitterProfile[1].values:
            count += 1
            document = language.types.Document(
                content=tweet,
                language='en',
                type=language.enums.Document.Type.PLAIN_TEXT,
            )
            response = client.analyze_sentiment(
                document=document,
                encoding_type='UTF32',
            )
            sentiment = response.document_sentiment
            profileSentiment.append(
                float(sentiment.score)
            )
            response = client.analyze_entities(document)
            for entity in response.entities:
                if entity.sentiment.score != 0.0:
                    profileSentiment.append(
                        entity.sentiment.score
                    )
                profileSentiment.append(
                    entity.sentiment.magnitude
                )
            if count == 45:
                break
        profileSentiment = list(dict.fromkeys(profileSentiment))
        amin, amax = -1, 1
        for i, val in enumerate(profileSentiment):
            profileSentiment[i] = (val-amin) / (amax-amin)
        mood = 1
        for num in profileSentiment:
            if num <= 0.01:
                if mood >= 2:
                    mood -= 1
            elif num <= 0.25:
                if mood >= 2:
                    mood -= 1
            elif num <= 0.45:
                if mood >= 2:
                    mood -= 1
            elif num < 0.53:
                if mood >= 2:
                    mood -= 1
            elif num >= 0.55:
                if mood <= 5:
                    mood += 1
            elif num >= 0.8:
                if mood <= 5:
                    mood += 1
            elif num >= 0.9:
                if mood >= 0.9:
                    mood += 1
        print(profileSentiment)
        return str(mood)

    else:
        return f'Hello World!'


