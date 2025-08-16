from flask import Flask
from app.controllers.c_hospede import hospede_bp

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False #Isso so para não ordenar meus atributos do banco de dados por ordem

#Aqui estou infromando que meu app recebe as funções do blueprint
app.register_blueprint(hospede_bp)

if __name__ == '__main__':
    app.run(debug=True)
    