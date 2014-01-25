class ImagesController < ApplicationController
  skip_before_action :verify_authenticity_token, only: [:create]

  def index
    # just for debugging
    render nothing: true
  end

  def show
    send_file Rails.root.join("public/images", "input.jpg"), type: "image/jpg", disposition: "inline"
  end

  # Always accept an image, but eventually we want this to store remixed
  # images.
  def create
    render nothing: true, status: 200
  end

end
