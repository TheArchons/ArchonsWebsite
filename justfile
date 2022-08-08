startOnlineFedora:
    cd /home/admin/ArchonsWebsite/ArchonsWebsite
    git pull
    gunicorn ArchonsWebsite.wsgi:application --bind 0.0.0.0:8000