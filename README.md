# mentiunq-backend
Backend of the apps mentiunq 
# create a venv with the version of python to use 
 virtualenv menti-env --python=/usr/bin/python3.8
# enter the venv
 source menti-env/bin/activate
# We install the requirements that we are going to use
 pip install -r requirements.txt
# we raise the database
 python manage.py migrate
# we create a superuser (only to enter the admin)
 python manage.py createsuperuser
# we raise the server
 python manage.py runserver

## raises on the following socket localhost:8000


