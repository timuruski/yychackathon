module ApplicationHelper
  def breadcrumb (*names)
    @breadcrumb = Array(names).map { |name| content_tag(:li, name) }
  end
end
