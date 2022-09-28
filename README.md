# mentiunq-backend
Backend of the apps mentiunq 

### We download project from this repository. Only god and you know how you got here

## Two ways to init the project

## Easy way
### We create docker container and raise server on 8000
`sudo docker-compose up -d --build`
### To run commands in `manage.py`
#### Now we must use it after `docker-compose exec web`
#### eg ***Migrate:*** `docker-compose exec web python manage.py migrate`
 


## The dark side
### Create a venv with the version of python to use
`virtualenv menti-env --python=/usr/bin/python3.8`

### Enter into virtual environment
`source menti-env/bin/activate`

### Install the requirements that we are going to use
`pip install -r requirements.txt`

### Raise the database
`python manage.py migrate`

### Create a superuser (only to enter the admin)
`python manage.py createsuperuser`

### Raise the server
`python manage.py runserver`

## Both ways raise server on the following socket localhost:8000

### Enjoy and coding 
### #12C  


