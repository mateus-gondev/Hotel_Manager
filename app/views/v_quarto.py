from flask import make_response
#Ainda em Desenvolvimento!!
# Função utilitária para exibir uma mensagem em popup e retornar à página anterior
def popup_message(message):
    html = f"""
    <script>
        alert("{message}");           // Exibe a mensagem no navegador
        window.history.back();        // Retorna para a página anterior
    </script>
    """
    return make_response(html, 200)  # Retorna o HTML como resposta HTTP com status 200

# Renderiza uma lista de todos os quartos disponíveis
def render_lista_quartos(quartos_dict):
    html = "<h1>Lista de Quartos</h1><ul>"  # Título da página e início da lista
    for qid, quarto in quartos_dict.items():  # Percorre cada quarto no dicionário
        # Mostra nome e status de ocupação
        html += f"<li>{qid}: {quarto['nome']} - {'Ocupado' if quarto['status'] else 'Disponível'}</li>"
    html += "</ul>"  # Final da lista
    return make_response(html, 200)  # Retorna a página como resposta HTTP

# Renderiza os detalhes de um quarto específico
def render_quarto(quarto):
    if quarto is None:
        return popup_message("Quarto não encontrado!")  # Se não existir, mostra erro
    html = f"<h1>Detalhes do Quarto</h1><p>{quarto}</p>"  # Exibe os dados do quarto
    return make_response(html, 200)

# Renderiza uma mensagem de sucesso ao criar um quarto
def render_quarto_criado(quarto):
    return popup_message("Quarto criado com sucesso!")

# Renderiza uma mensagem ao deletar um quarto (sucesso ou erro)
def render_quarto_deletado(sucesso):
    if sucesso is None:
        return popup_message("Quarto não encontrado!")  # Se o quarto não existir
    return popup_message("Quarto deletado com sucesso!")  # Se for deletado corretamente

# Renderiza uma mensagem ao atualizar um quarto (sucesso ou erro)
def render_quarto_atualizado(sucesso):
    if sucesso is None:
        return popup_message("Quarto não encontrado!")  # Se o quarto não existir
    return popup_message("Quarto atualizado com sucesso!")  # Se for atualizado corretamente
