from app import myapp,db,celery,start_sleep
from celery.result import *
from forms import TaskForm
from flask import render_template, flash, redirect, session, url_for, request,g
from models import Task

@myapp.route('/tasks', methods = ['GET','POST'])
def tasks():
	# imported our TaskForm class, instantiated an object from it,
	#and sent it down to the template where forms is used.
	form = TaskForm(request.form)
	tasks = Task.query.all()
	# for task in tasks:
	# 	db.session.delete(task)
	# db.session.commit()
	
	#print "REQUEST HUI: ",request.form['numberOfSeconds']
	if request.method == 'POST' and form.validate_on_submit():
		flash('Created Async Task!')
		#save numberOfSeconds in a session hash
		session['numberOfSeconds'] = form.numberOfSeconds.data
		time = int(session['numberOfSeconds'])
		#START OF ASYNC SLEEP CALL#
		t1 = start_sleep.delay(time)
		session['TASK_ID'] = t1.id
		#add new async task to database
		new_task = Task(time = int(session['numberOfSeconds']),status= t1.ready(),key =session['TASK_ID'])
		db.session.add(new_task)
		db.session.commit()
		for i in tasks:
			print"AYYYEEEEE %s %s %s %s" % (i.id,i.time,i.status,i.key)
		return redirect(url_for('tasks'))
	return render_template('tasks.html',
					title = 'Amadeus Task', 
					form = form,
					tasks = tasks)

@myapp.route('/tasks/<int:id>')
def specific_task(id):
	tasks = Task.query.all()
	for task in tasks:
		task.status = celery.AsyncResult(task.key).status
		print task.status
	return render_template('status.html',
							id=id,
							tasks=tasks)

	
