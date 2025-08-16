from flask import request


from model.m_quarto import (
    get_todos_quartos,
    get_quarto,
    adicionar_quarto,
    atualizar_quarto,
    deletar_quarto
)
from views.v_quarto import (
    render_lista_quartos,
    render_quarto,
    render_quarto_criado,
    render_quarto_deletado,
    render_quarto_atualizado,
    popup_message
)

def configurar_rotas(app):
    # Listar todos os quartos
    @app.route("/", methods=["GET"])
    def listar_quartos():
        quartos = get_todos_quartos()
        return render_lista_quartos(quartos)

    # Obter detalhes de um quarto específico
    @app.route("/quarto/<int:quarto_id>", methods=["GET"])
    def obter_quarto(quarto_id):
        quarto = get_quarto(quarto_id)
        return render_quarto(quarto)

    # Criar um novo quarto
    @app.route("/quarto", methods=["POST"])
    def criar_quarto():
        nome = request.form.get("nome")
        if not nome:
            return popup_message("Nome do quarto é obrigatório.")
        quarto = adicionar_quarto(nome)
        return render_quarto_criado(quarto)

    # Atualizar um quarto existente
    @app.route("/quarto/<int:quarto_id>", methods=["POST"])
    def atualizar_quarto_endpoint(quarto_id):
        nome = request.form.get("nome")
        status = request.form.get("status")
        status_bool = status.lower() == "true" if status else None
        resultado = atualizar_quarto(quarto_id, nome=nome, status=status_bool)
        return render_quarto_atualizado(resultado)

    # Deletar um quarto
    @app.route("/quarto/<int:quarto_id>/deletar", methods=["POST"])
    def deletar_quarto_endpoint(quarto_id):
        resultado = deletar_quarto(quarto_id)
        return render_quarto_deletado(resultado)
