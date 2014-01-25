class InterestingTweetsController < ApplicationController
  before_action :set_interesting_tweet, only: [:show, :edit, :update, :destroy]

  # GET /interesting_tweets
  # GET /interesting_tweets.json
  def index
    @interesting_tweets = InterestingTweet.all
  end

  # GET /interesting_tweets/1
  # GET /interesting_tweets/1.json
  def show
    @interesting_tweets = InterestingTweet.all
  end

  # GET /interesting_tweets/new
  def new
    @interesting_tweet = InterestingTweet.new
  end

  # GET /interesting_tweets/1/edit
  def edit
  end

  # POST /interesting_tweets
  # POST /interesting_tweets.json
  def create
    @interesting_tweet = InterestingTweet.new(interesting_tweet_params)

    respond_to do |format|
      if @interesting_tweet.save
        format.html { redirect_to @interesting_tweet, notice: 'Interesting tweet was successfully created.' }
        format.json { render action: 'show', status: :created, location: @interesting_tweet }
      else
        format.html { render action: 'new' }
        format.json { render json: @interesting_tweet.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /interesting_tweets/1
  # PATCH/PUT /interesting_tweets/1.json
  def update
    respond_to do |format|
      if @interesting_tweet.update(interesting_tweet_params)
        format.html { redirect_to @interesting_tweet, notice: 'Interesting tweet was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: 'edit' }
        format.json { render json: @interesting_tweet.errors, status: :unprocessable_entity }
      end
    end
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
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def interesting_tweet_params
      params[:interesting_tweet]
    end
end
