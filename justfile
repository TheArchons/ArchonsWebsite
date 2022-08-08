startOnlineFedora:
    cd /home/admin/ARCHONSWEBSITE/ArchonsWebsite
    git pull
    nohup python3 -u manage.py runserver 0.0.0.0:8000