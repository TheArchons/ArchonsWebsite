StartOnlineDebian:
    cd /home/archons/ArchonsWebsiteRedesign
    git pull
    RAILS_ENV=production /home/archons/.rbenv/shims/rails assets:precompile
    nohup /home/archons/.rbenv/shims/rackup -E production