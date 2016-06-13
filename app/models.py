from app import db

#database models (how information is represented)
class Task(db.Model):
	#unique identifier
	id = db.Column(db.Integer, primary_key=True)
	#time.sleep(n) where n represents time in seconds
	time = db.Column(db.Integer)
	#current status of task (is it finished/not finished?)
	status = db.Column(db.Boolean)
	#Asyncresult key to track status
	key = db.Column(db.String(120))

	def __repre__(self):
		return '<ID: %r TIME: %r STATUS: %r >' % (self.id, self.time, self.status)
