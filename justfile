StartOnlineDebian:
    cd /home/archons/ArchonsWebsiteRedesign
    git pull
    RAILS_ENV=production rails assets:precompile
    nohup /home/archons/.rbenv/shims/rackup -E production