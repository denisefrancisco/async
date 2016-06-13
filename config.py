import os
basedir = os.path.abspath(os.path.dirname(__file__))

#sql alchemy database uri is required by sqlalchemy extension. path of db!
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'app.db')
#migrate repo is the folder where the sqlalchemy-migrate data files are stored!
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
CELERY_BROKER_URL='amqp://guest@localhost:5672//',
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
