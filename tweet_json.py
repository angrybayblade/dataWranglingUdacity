import tweepy
from tqdm import tqdm
import pandas as pd
from timeit import default_timer as timer
import json

df_1 = pd.read_csv("twitter-archive-enhanced.csv")

consumer_key = "mCML3E699gwX9WzvAzje3bH56"
consumer_secret= "hXlhhtJk0asnJIpaWJv8rRPhlb6LTwT3oRVZTLF0PxaskaHcGY"
access_token = "927062798433058816-Ron9X5VMoPF4rO84sIA1XDKEnR1HNOR"
access_token_secret = "GXmRJ52smNx8pCiDaYapSXqNUWT7Mlht2UYmKWZuIRWsl"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

tweet_ids = df_1.tweet_id.values
len(tweet_ids)

count = 0
fails_dict = {}
start = timer()

with open('tweet_json.txt', 'w') as outfile:
    for tweet_id in tqdm(tweet_ids):
        count += 1
        print(str(count) + ": " + str(tweet_id))
        try:
            tweet = api.get_status(tweet_id, tweet_mode='extended')
            print("Success")
            json.dump(tweet._json, outfile)
            outfile.write('\n')
        except tweepy.TweepError as e:
            print("Fail")
            fails_dict[tweet_id] = e
            pass

end = timer()

print(end - start)
print(fails_dict)
