from app import app, db
from flask import render_template, url_for, request

from app.models import Contato

from app.forms import ContatoForm

@app.route('/')
def homepage():
    usuario = 'Kauan Turcato Storto'
    return render_template('index.html', usuario=usuario)


@app.route('/contato_old/', methods=['GET', 'POST'])
def contatopageold():
        if request.method == 'GET':
            pesquisa = request.args.get('pesquisa')

        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            assunto = request.form['assunto']
            mensagem = request.form['mensagem']

            contato = Contato (
                nome=nome,
                email=email,
                assunto=assunto,
                mensagem=mensagem   
            )

            db.session.add(contato)
            db.session.commit()
              
              
        return render_template('contato_old.html')

@app.route('/contato/', methods=['GET', 'POST'])
def contatopage():
    form = ContatoForm()   
    if form.validate_on_submit():
        form.save()
              
    return render_template('contato.html', form=form)