# cofing: utf-8
import twitter
import secret
import json
from GenerateText import GenerateText

def markovbot():
    api = twitter.Api(
            consumer_key = secret.twDict['consumer_key'],
            consumer_secret = secret.twDict['consumer_secret'],
            access_token_key = secret.twDict['access_token_key'],
            access_token_secret = secret.twDict['access_token_secret'])

    generator = GenerateText()
    gen_txt = generator.generate()
    tweet_txt = gen_txt + "[from bot]"
    print(tweet_txt)
    status = api.PostUpdate(tweet_txt)
    #print(status.text)

if __name__ == '__main__':
        markovbot()
