from flask import Blueprint, make_response, jsonify, request
from app.bd import Hospede

# Aqui vou esta declarando o Blueprint para "modularizar" quebrar o sistema em partes menores
hospede_bp = Blueprint('hospede', __name__)

#Rota para mostrar nossa lista com os hospedes
@hospede_bp.route('/hospede', methods=['GET'])
def get_hospedes():
    return make_response (
        jsonify(
                mensagem="Listados Hospedes",
                dados=Hospede
            )
    )

@hospede_bp.route('/hospede', methods=['POST'])
def create_hospede():
    hospede = request.json
    Hospede.append(hospede)
    return make_response (
        jsonify(
                mensagem="Hospedes Cadastardo com sucesso!",
                hospede=hospede
            )
    ) 


