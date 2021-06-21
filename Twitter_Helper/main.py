import twitter, json
from datetime import datetime, timedelta, timezone

# Replace empty string with actual value
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

# Select the last day you want to preserve
days_to_keep = 100
cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_to_keep)

file = open("twitter_data/data/tweet.js","r", encoding='UTF-8')
myTweets = json.loads(file.read()) #file.read() because I want to pass the file content, not the file object itself


for tweet in myTweets:
    temp_date = datetime.strptime(tweet['tweet']['created_at'], "%a %b %d %H:%M:%S %z %Y")
    if temp_date < cutoff_date:
        try:              
            id = int(tweet['tweet']['id_str'])
            api.DestroyStatus(id)      
        except Exception as e:
            print(e)
            pass

    # The rest of the tweets are after the cutoff date
    else:
        break



