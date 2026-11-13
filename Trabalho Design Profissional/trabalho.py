# ==========================================
#   SISTEMA SIMPLES DE LOCADORA DE FILMES
# ==========================================
 
# Lista de filmes (cada filme é um dicionário)
filmes = [
    {"id": 1, "titulo": "O Poderoso Chefão", "preco": 8.00, "disponivel": True},
    {"id": 2, "titulo": "Matrix", "preco": 6.50, "disponivel": True},
    {"id": 3, "titulo": "Vingadores: Ultimato", "preco": 9.00, "disponivel": True},
    {"id": 4, "titulo": "Interestelar", "preco": 7.50, "disponivel": True},
    {"id": 5, "titulo": "Toy Story", "preco": 5.00, "disponivel": True},
]
 
# Lista de clientes cadastrados (guarda só os nomes)
clientes = []
 
# Lista de aluguéis ativos (cliente + filme)
alugueis = []
 
 
def mostrar_menu():
    print("\n===== LOCADORA DE FILMES =====")
    print("1 - Listar filmes")
    print("2 - Cadastrar cliente")
    print("3 - Alugar filme")
    print("4 - Devolver filme")
    print("5 - Ver filmes alugados")
    print("0 - Sair")
 
 
def listar_filmes():
    print("\n--- Catálogo de Filmes ---")
    for filme in filmes:
        if filme["disponivel"]:
            status = "Disponível"
        else:
            status = "Alugado"
        print(f"{filme['id']} - {filme['titulo']} | R$ {filme['preco']:.2f} | {status}")
 
 
def cadastrar_cliente():
    nome = input("Nome do cliente: ").strip()
    if nome == "":
        print("Nome não pode ser vazio!")
    elif nome in clientes:
        print("Esse cliente já está cadastrado!")
    else:
        clientes.append(nome)
        print(f"Cliente {nome} cadastrado com sucesso!")
 
 
def buscar_filme(id_filme):
    # Procura o filme pelo id e retorna ele (ou None se não achar)
    for filme in filmes:
        if filme["id"] == id_filme:
            return filme
    return None
 
 
def alugar_filme():
    nome = input("Nome do cliente: ").strip()
    if nome not in clientes:
        print("Cliente não cadastrado! Cadastre primeiro (opção 2).")
        return
 
    listar_filmes()
    try:
        id_filme = int(input("Digite o ID do filme que deseja alugar: "))
    except ValueError:
        print("Digite apenas números!")
        return
 
    filme = buscar_filme(id_filme)
    if filme is None:
        print("Filme não encontrado!")
    elif not filme["disponivel"]:
        print("Esse filme já está alugado!")
    else:
        filme["disponivel"] = False
        alugueis.append({"cliente": nome, "filme": filme["titulo"]})
        print(f"{nome} alugou '{filme['titulo']}'. Valor: R$ {filme['preco']:.2f}")
 
 
def devolver_filme():
    if len(alugueis) == 0:
        print("Nenhum filme alugado no momento.")
        return
 
    nome = input("Nome do cliente: ").strip()
    titulo = input("Título do filme a devolver: ").strip()
 
    for aluguel in alugueis:
        if aluguel["cliente"] == nome and aluguel["filme"].lower() == titulo.lower():
            alugueis.remove(aluguel)
            for filme in filmes:
                if filme["titulo"] == aluguel["filme"]:
                    filme["disponivel"] = True
            print("Filme devolvido com sucesso!")
            return
 
    print("Aluguel não encontrado. Confira o nome e o título.")
 
 
def ver_alugueis():
    print("\n--- Filmes Alugados ---")
    if len(alugueis) == 0:
        print("Nenhum filme alugado.")
    else:
        for aluguel in alugueis:
            print(f"{aluguel['cliente']} está com '{aluguel['filme']}'")
 
 
# ---------- PROGRAMA PRINCIPAL ----------
opcao = ""
while opcao != "0":
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
 
    if opcao == "1":
        listar_filmes()
    elif opcao == "2":
        cadastrar_cliente()
    elif opcao == "3":
        alugar_filme()
    elif opcao == "4":
        devolver_filme()
    elif opcao == "5":
        ver_alugueis()
    elif opcao == "0":
        print("Encerrando o sistema. Até logo!")
    else:
        print("Opção inválida! Tente de novo.")
 