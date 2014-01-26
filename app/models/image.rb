class Image < ActiveRecord::Base
  # Or just use the media_id?
  belongs_to :interesting_tweet
end
