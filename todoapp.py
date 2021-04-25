'''
Part II and Part III
'''

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import re

app = Flask(__name__)

todo_list = []

@app.route('/')
def display_list():
    # display
    return render_template('todo.html', todo_list=todo_list)


@app.route('/submit', methods=["POST"])
def submit():
    """
    Processing the data
    """
    global todo_list

    task = request.form['task']
    print(task)
    email = request.form['email']
    priority = request.form['priority']
    #domain could be any number of characters, .hacker, .forum, .edu - something@something.something
    if(priority == "Low" or priority == "Medium" or priority =="High") and re.search(r"\w+[@]\w+[.]\w+", email):
        todo_list.append((task, email, priority))
        return redirect(url_for('display_list'))
    else:
        return redirect(url_for('display_list'))


@app.route('/clear', methods=["POST"])
def clear():
    """
    Clear the list
    """
    global todo_list

    todo_list = []
    return redirect(url_for('display_list'))

@app.route('/delete', methods=["POST"])
def delete():
    """
     Extra Credit II: Delete Individual Items
    """
    global todo_list

    Task = request.form.get('Task')
    Email = request.form.get('Email')
    Priority = request.form.get('Priority')

    todo_list.remove((Task, Email, Priority))

    return redirect(url_for('display_list'))


if __name__ == '__main__':
    app.run(debug=True)
