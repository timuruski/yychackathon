class RepliesController < ApplicationController
  def create
    @reply = Reply.new(reply_params)

    respond_to do |format|
      if @reply.save
        format.html { redirect_to '/interesting_tweets/1', notice: 'Reply was successfully created.' }
        format.json { render action: 'show', status: :created, location: @reply }
      else
        format.html { render action: 'new' }
        format.json { render json: @reply.errors, status: :unprocessable_entity }
      end
    end
  end

  private

  def reply_params
    params.require(:reply).permit(:text, :interesting_tweet_id)
  end
end
