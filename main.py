from flask import Flask

from app import app
#Inicia apenas de se o nome da pagina for main
if __name__ == '__main__':
    #Rodar pagina com debug atividado
    app.run(debug=True)