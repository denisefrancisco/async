#script creates application object and imports views module.
#DO NOT CONFUSE app the variable (which gets assigned to flask instance)
#to app the package (from which we import the views module).
from flask import Flask
from celery import Celery
from flask.ext.sqlalchemy import SQLAlchemy
import time

#Flask app initialization
myapp = Flask(__name__)
myapp.config.from_object('config')
myapp.config.update(
	#messaging broker
    CELERY_BROKER_URL='amqp://guest@localhost:5672//',
    #allow to save results of task states
    CELERY_RESULT_BACKEND='amqp',
    )

#function to create Celery object instance
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
