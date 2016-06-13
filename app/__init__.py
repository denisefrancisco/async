#script creates application object and imports views module.
#DO NOT CONFUSE app the variable (which gets assigned to flask instance)
#to app the package (from which we import the views module).
from flask import Flask
from celery import Celery
from flask.ext.sqlalchemy import SQLAlchemy
# from tasks import *
#from app.celery import start_sleep
import time

myapp = Flask(__name__)
myapp.config.from_object('config')
myapp.config.update(
    CELERY_BROKER_URL='amqp://guest@localhost:5672//',
    CELERY_RESULT_BACKEND='amqp',
    CELERY_RESULT_PERSISTENT = True
    )

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    return celery


#initializing celery
celery = make_celery(myapp)
celery.conf.update(myapp.config)

#initializing the database
db = SQLAlchemy(myapp) 

#START OF CELERY FUNCTION BLOCK#
@celery.task()
def start_sleep(n):
    print "start time"
    time.sleep(n)
    print "end time"
#END OF CELERY FUNCTION BLOCK#

from app import views, models
#views - web page interfaces
#models - structure of database, structure of info of data.
