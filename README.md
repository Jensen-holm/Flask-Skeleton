# Flask-Skeleton
Flask web app skeleton

### Run Locally
$ pip3 install -r requirements.txt
$ gunicorn --bind :3000 --workers 1 --threads 8 --timeout 0 app:app
