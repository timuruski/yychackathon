class CreateInterestingTweets < ActiveRecord::Migration
  def change
    create_table :interesting_tweets do |t|
      t.string   :tweet_id
      t.string   :image_url
      t.string   :username
      t.datetime :created_at
      t.float    :latitude
      t.float    :longitude
      t.text     :raw
    end
  end
end
