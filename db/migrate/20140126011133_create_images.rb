class CreateImages < ActiveRecord::Migration
  def change
    create_table :images do |t|
      t.references :interesting_tweet
      t.string     :original_url
      t.string     :media_id
      t.binary     :data
    end
  end
end
