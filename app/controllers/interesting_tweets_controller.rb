class InterestingTweetsController < ApplicationController
  before_action :set_interesting_tweet, only: [:show, :edit, :update, :destroy]

  # GET /interesting_tweets
  # GET /interesting_tweets.json
  def index
    @interesting_tweets = InterestingTweet.all
    render 'index_fake'
  end

  # GET /interesting_tweets/1
  # GET /interesting_tweets/1.json
  def show
    @interesting_tweets = InterestingTweet.all
    @reply = Reply.new
    render 'show_fake'
  end

  # DELETE /interesting_tweets/1
  # DELETE /interesting_tweets/1.json
  def destroy
    @interesting_tweet.destroy
    respond_to do |format|
      format.html { redirect_to interesting_tweets_url }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_interesting_tweet
      @interesting_tweet = InterestingTweet.find(params[:id])
    rescue ActiveRecord::RecordNotFound
      @interesting_tweet = InterestingTweet.new do |tweet|
        tweet.username = 'timuruski'
      end
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def interesting_tweet_params
      params[:interesting_tweet]
    end
end
