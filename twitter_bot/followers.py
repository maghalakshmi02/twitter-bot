#METHOD FOR FOLLOWERS
for follower in tweepy.Cursor(api.followers).items():
  follower.follow()
  def user():
   print("Followed everyone that is following" + user.name)
