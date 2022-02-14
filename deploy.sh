#!/bin/sh     
<<<<<<< HEAD
sudo git pull origin main
=======
sudo git pull origin master
>>>>>>> 332882518a80e94d1be758cb79bc912ce664cd6f
sudo pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
sudo systemctl restart nginx
<<<<<<< HEAD
sudo systemctl restart gunicorn
=======
sudo systemctl restart gunicorn
>>>>>>> 332882518a80e94d1be758cb79bc912ce664cd6f
