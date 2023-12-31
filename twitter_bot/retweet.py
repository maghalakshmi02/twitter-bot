#METHOD FOR RETWEET
search = "#keyword"
numberofTweets = "no.of counts to be needed to like"
for tweet in tweepy.Cursor(api.search,search).items(10):
    try:
      tweet.retweet()
      print('Retweeted')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
