class CreateReplies < ActiveRecord::Migration
  def change
    create_table :replies do |t|
      t.integer :interesting_tweet_id
      t.integer :image_id
      t.string :text

      t.timestamps
    end
  end
end
