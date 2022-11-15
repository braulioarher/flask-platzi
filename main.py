import unittest
from flask import request, make_response, redirect, render_template, session, flash, url_for
from flask_login import login_required, current_user

from app import create_app
from app.forms import LoginForm, TodoForm, TodoDeleteForm, UpdateTodoForm
from app.firestore_service import get_todos, put_todo, delete_todo, update_todo

app = create_app()

todos = ['Comparar cafe', 'Enviar solicitud de compra', 'Entregar video al productor']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error = error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error = error)

@app.route('/') ## se crea esta ruta para redireccionar a route automaticamente
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response

#Definimos la ruta de inicio de nuestra aplicacion con un decorador
@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    delete_form = TodoDeleteForm()
    update_form = UpdateTodoForm()
    context = {
        'user_ip': user_ip, 
        'todos': get_todos(username),
        'username': username,
        'todo_form' : todo_form,
        'delete_form' : delete_form,
        'update_form' : update_form
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)

        flash('Tarea agregada con exito')

        return redirect(url_for('hello'))


    return render_template('hello.html', **context)

#Ruta dinamica de flask se defini entre los simbolos <>
@app.route('/todo/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('hello'))

@app.route('/todo/update/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id
    update_todo(user_id, todo_id, done)
    
    return redirect(url_for('hello'))


