#METHOD FOR LIKE\FAVOURITES
search = "#keyword you want"
numberofTweets = "no.of counts to be needed to like"
for tweet in tweepy.Cursor(api.search,search).items(10):
    try:
      tweet.favorite()
      print('liked')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

