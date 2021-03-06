# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20140126011133) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "images", force: true do |t|
    t.integer "interesting_tweet_id"
    t.string  "original_url"
    t.string  "media_id"
    t.binary  "data"
  end

  create_table "interesting_tweets", force: true do |t|
    t.string   "tweet_id"
    t.string   "image_url"
    t.string   "username"
    t.datetime "created_at"
    t.float    "latitude"
    t.float    "longitude"
    t.text     "raw"
    t.string   "text"
  end

  create_table "replies", force: true do |t|
    t.integer  "interesting_tweet_id"
    t.integer  "image_id"
    t.string   "text"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

end
