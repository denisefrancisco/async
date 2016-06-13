from app import db

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	time = db.Column(db.Integer)
	status = db.Column(db.Boolean)
	key = db.Column(db.String(120))

	def __repre__(self):
		return '<ID: %r TIME: %r STATUS: %r >' % (self.id, self.time, self.status)
