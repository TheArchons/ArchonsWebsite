class HomeController < ApplicationController
  def index
    @blocks = Block.all
    @profile_entries = profileEntry.all
  end
end
