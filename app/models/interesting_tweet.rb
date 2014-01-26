class InterestingTweet < ActiveRecord::Base
  serialize :raw, JSON

  def excerpt
    text[0..20]
  end

  def image_url
    "http://placekitten.com/200/300"
  end

end
