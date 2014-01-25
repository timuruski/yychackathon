module InterestingTweetsHelper
  def current?(tweet)
    @interesting_tweet == tweet
  end
end
