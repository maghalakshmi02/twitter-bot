import tweepy
#credentials of the ID
consumer_key = 'i4wPGsQUGCDevufntXe8vavQ1'
consumer_secret = 'jTGMg037dW7eFy3OQlhBc150q0X6XeZV2xmEAgGvMD8OimPBZQ'
access_token = '1599298879605772288-gwsdbxfcGiXI6VDhV5V9GTR4brGfEs'
access_token_secret = 'SgLOat5xnY6Ze1iCDk0m9EQiqIwyJxMpPa4PJG3EuEA5n'
#METHOD FOR TWEETS
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api = tweepy.API(auth)
api.update_status('project completed')
