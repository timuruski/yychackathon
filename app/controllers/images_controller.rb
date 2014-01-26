class ImagesController < ApplicationController
  skip_before_action :verify_authenticity_token, only: [:create]
  before_action :set_image, only: [:show]

  def index
    render nothing: true
  end

  def show
    send_data @image.data, type: "image/jpg", disposition: "inline"
  end

  def set_image
    @image = Image.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    path = Rails.root.join("public/images", "input.jpg")
    @image = Image.new(data: File.read(path))
  end

  # Always accept an image, but eventually we want this to store remixed
  # images.
  def create
    render nothing: true, status: 200
  end

end
