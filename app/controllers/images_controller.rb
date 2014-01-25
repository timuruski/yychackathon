class ImagesController < ApplicationController
  # protect_from_forgery false
  skip_before_action :verify_authenticity_token, only: [:create]

  def index
    # just for debugging
  end

  def show
    send_file Rails.root.join("public/images", "input.jpg"), type: "image/jpg", disposition: "inline"
  end

  def create
    # This always works
    render nothing: true, status: 200
  end

end
