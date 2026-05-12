from flask import Flask

#Iniciar Projeto __name__ irá receber o nome do projeto.
app = Flask(__name__)

#Criar uma rota, rota são "site.com/", tudo após o barra
@app.route('/')
#Criar Pagina
def homepage():
    return 'Minha pagina flask'

#Inicia apenas de se o nome da pagina for main
if __name__ == '__main__':
    #Rodar pagina com debug atividado
    app.run(debug=True)