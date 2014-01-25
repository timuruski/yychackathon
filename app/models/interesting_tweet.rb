class InterestingTweet < ActiveRecord::Base
  serialize :raw, JSON

  def excerpt
    text[0..20]
  end

end
