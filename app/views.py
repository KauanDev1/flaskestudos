from app import app
from flask import render_template, url_for, request

@app.route('/')
def homepage():
    usuario = 'Kauan Turcato Storto'
    return render_template('index.html', usuario=usuario)

@app.route('/contato/', methods=['GET', 'POST'])
def contatopage():
        if request.method == 'GET':
            pesquisa = request.args.get('pesquisa')

        if request.method == 'POST':
            pesquisa = request.form['pesquisa']
              
              
        return render_template('contato.html', pesquisa=pesquisa)