from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus.reader import wordnet
import nltk
import re
import pandas as pd
import os

from tweepy import OAuthHandler
from tweepy import API

def getTweets(request):
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

        class CleanText:

            @staticmethod
            def remove_stopwords(string: str):
                """
                Removes all the stop words in a string
                :param string: the string
                :return: a new containing no stop words
                """

                stop_words = set(stopwords.words('english'))
                return ' '.join([word for word in string.split() if word not in stop_words])

            @staticmethod
            def remove_non_letters(string: str):
                """
                Removes non letters from string.
                :param string: The string.
                :return: A string with only lowercase letters.
                """

                # Remove non_letters, separate by space, the string, lowercase
                new_string = re.sub('[^a-zA-Z]', ' ', string).lower()
                # To list, to string
                # To remove whitespace
                string = ' '.join(new_string.split())
                return string.replace('\n', '')

            @staticmethod
            def stem_string(string: str):
                stemmer = PorterStemmer()
                return ' '.join([stemmer.stem(word=word) for word in string.split()])

            @staticmethod
            def wordnet_lemmatizer(string: str):
                tag_dict = {'J': wordnet.ADJ, 'N': wordnet.NOUN, 'V': wordnet.VERB, 'R': wordnet.ADV}
                lemmatizer = WordNetLemmatizer()
                new_string = []
                for word in string.split():
                    tag = nltk.pos_tag([word])[0][1][0].upper()
                    if tag in tag_dict:
                        word = lemmatizer.lemmatize(word, pos=tag_dict[tag])
                    else:
                        word = lemmatizer.lemmatize(word, pos=wordnet.NOUN)

                    new_string.append(word)
                return ' '.join(new_string)
                # return ' '.join([lemmatizer.lemmatize(word) for word in string.split()])

            @staticmethod
            def remove_links(string: str):
                """
                Removes the links in the string
                :param string: The new string.
                :return: A string.
                """

                return ' '.join([s for s in string.split() if 'http' not in s])

            @staticmethod
            def remove_rp_text(string: str):
                """
                Removes the 'RP @' text
                :param string:
                :return:
                """

                new_string = []
                for str_ in string.split():
                    if str_.startswith('RP @'):
                        str_ = str_[4:]
                        new_string.append(str_)
                    elif str_.startswith('rt '):
                        str_ = str_[4:]
                        new_string.append(str_)
                    else:
                        pass

            @staticmethod
            def clean_string(string: str):
                # text = CleanText.remove_links(string)
                text = CleanText.remove_non_letters(string)
                # text = CleanText.remove_stopwords(text)
                # text = CleanText.wordnet_lemmatizer(text)
                return text


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
        tweets = auth_api.user_timeline(screen_name=person, count=500, tweet_mode="extended")
        cleaned_tweets = []
        cleaner = CleanText()
        for tweet in tweets:
            tweet = tweet.full_text
            tweet = cleaner.clean_string(tweet)
            # if not tweet.startswith('RT @'):
            #     cleaned_tweets.append(tweet)
            cleaned_tweets.append(tweet)

        dataset = pd.DataFrame(data=cleaned_tweets, columns=None, index=None)

        return dataset.to_csv()

    else:
        return f'Hello World!'