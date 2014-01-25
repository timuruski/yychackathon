class AddTextToTweets < ActiveRecord::Migration
  def change
    add_column :interesting_tweets, :text, :string
  end
end
