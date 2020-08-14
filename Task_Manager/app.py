from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#setting up our application
app = Flask(__name__)

#Tell our app where our dB is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db is being initialized 
db = SQLAlchemy(app)

#create a model
class Todo(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	content = db.Column(db.String(200), nullable = False) #we dont want user to create empty task
	date_created = db.Column(db.DateTime, default = datetime.utcnow)


#function that's going to return a string every time we create a new element
def __repr__(self):
	return '<Task %r>' % self.id 
	#everytime we make a new element, it'll return task and the id of task that's just been created
'''	
The %s and %r format specifier converts any object to string
!! the %r specifier takes the string as it is
'''

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
How to set up dB:
open terminal and go to directy, then write "python" in CL to open shell
then write "from app import db" in CL
then write "db.create_all()" in CL to create the dB; it opens a db file in our directory called "test.db", which was said in sqlite
then wrtie "exit()" in CL to exit out of shell
'''




#creating index route, so when we browse to the url, 
#we don't immediatly 404
#the 404 error code is when website content has been removed or moved to another URL
@app.route('/', methods = ['POST', 'GET']) 
#the get method is there by default, but now we can add Post, to send data to our dB



#creating a function for route
def index():

	#enters the if statement when you submit a form(when you press the button)
	if request.method == "POST":
		task_content = request.form['content'] #pass the id of the string input we submitted by clicking on the button
		new_task = Todo(content = task_content) #name of column is content; the rest of column value are added automatically

		try: #try to push to our dB
			db.session.add(new_task)
			db.session.commit()
			return redirect('/') #have a redirect back to our index page

		except:
			return 'There was an issue adding your task'


	#putting the dB records in index table here
	else:
		#querying the dB content and return all of them in ascending order of date_created column
		tasks = Todo.query.order_by(Todo.date_created).all()
		return render_template('indexx.html', tasks = tasks) #setting tasks to the variable we just created

	#return render_template('indexx.html') #this file needs to be in the templates folder, or can't be found

# adding a <> in the route makes it dynamic; int: is just a type check for the variable
#want to reference the record with it's PK
@app.route('/delete/<int:id>') 

def delete(id):
	task_to_delete = Todo.query.get_or_404(id) #it'll find the record or it'll go into 404 error

	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/') #going back to our home page

	except:
		return "There was a problem deleting that task"


@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
	task = Todo.query.get_or_404(id)

	if request.method == "POST":
		task.content = request.form['content'] #setting the new string submitted as the content of the task

		try:
			db.session.commit() #updated a dB record in line 94 so now im committing it
			return redirect('/')

		except:
			return "There was a problem updating your task"

	else:
		return render_template('update.html', task = task)



if __name__ == "__main__":
	app.run(debug=True) #bugs will pop up in webpage if there's any




#when I run this script, it starts a webserver called localhost