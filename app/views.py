from app import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    usuario = 'Kauan Turcato Storto'
    return render_template('index.html', usuario=usuario)

@app.route('/nova/')
def novapage():
    return 'Nova Pagina'