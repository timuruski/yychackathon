json.array!(@interesting_tweets) do |interesting_tweet|
  json.extract! interesting_tweet, :id
  json.url interesting_tweet_url(interesting_tweet, format: :json)
end
