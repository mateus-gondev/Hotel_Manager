#Ainda em Desenvolvimento!!
# Banco de dados em memória (dicionário que simula um banco)
quartos = {
    1: {"nome": "Quarto 1", "status": False},  # status=False significa "Disponível"
    2: {"nome": "Quarto 2", "status": True}    # status=True significa "Ocupado"
}

# Função para buscar todos os quartos
def get_todos_quartos():
    return quartos  # Retorna o dicionário completo de quartos

# Função para buscar um quarto específico pelo ID
def get_quarto(quarto_id):
    return quartos.get(quarto_id)  # Retorna o quarto com o ID informado, ou None se não existir

# Função para adicionar um novo quarto
def adicionar_quarto(nome):
    # Gera novo ID sequencial (máximo existente + 1) ou 1 se a lista estiver vazia
    novo_id = max(quartos.keys()) + 1 if quartos else 1
    
    # Cria o novo quarto com nome informado e status padrão como "Disponível" (False)
    quartos[novo_id] = {"nome": nome, "status": False}
    
    # Retorna o novo quarto adicionado, como dicionário com ID
    return {novo_id: quartos[novo_id]}

# Função para atualizar nome e/ou status de um quarto existente
def atualizar_quarto(quarto_id, nome=None, status=None):
    if quarto_id not in quartos:
        return None  # Retorna None se o quarto não existir
    
    # Atualiza o nome, se fornecido
    if nome is not None:
        quartos[quarto_id]["nome"] = nome
    
    # Atualiza o status, se fornecido (True = Ocupado, False = Disponível)
    if status is not None:
        quartos[quarto_id]["status"] = status

    # Retorna o quarto atualizado
    return {quarto_id: quartos[quarto_id]}

# Função para deletar um quarto pelo ID
def deletar_quarto(quarto_id):
    # Remove o quarto e retorna seus dados, ou None se o ID não existir
    return quartos.pop(quarto_id, None)
