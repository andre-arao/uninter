print("Bem-vindos à empresa do André Matheus de Paula Arão")

# Lista de funcionários e ID global inicial
lista_funcionarios = []
id_global = 4916426  # Número do meu RU

# Função para cadastrar um funcionário
def cadastrar_funcionario(id):
    import copy
    global lista_funcionarios
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    
    # Adiciona o funcionário à lista de funcionários
    lista_funcionarios.append(copy.deepcopy(funcionario))

# Função para consultar funcionários
def consultar_funcionarios():
    while True:
        print("\nOpções de Consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            if not lista_funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                for func in lista_funcionarios:
                    print(func)
        elif opcao == "2":
            id = int(input("Digite o ID do funcionário: "))
            encontrado = False
            for func in lista_funcionarios:
                if func['id'] == id:
                    print(func)
                    encontrado = True
                    break
            if not encontrado:
                print("ID inválido.")
        elif opcao == "3":
            setor = input("Digite o setor: ")
            encontrados = [func for func in lista_funcionarios if func['setor'] == setor]
            if encontrados:
                for func in encontrados:
                    print(func)
            else:
                print("Nenhum funcionário encontrado para o setor informado.")
        elif opcao == "4":
            return
        else:
            print("Opção inválida. Tente novamente.")

# Função para remover um funcionário
def remover_funcionario():
    global lista_funcionarios
    id = int(input("Digite o ID do funcionário a ser removido: "))
    removido = False
    for i, func in enumerate(lista_funcionarios):
        if func['id'] == id:
            lista_funcionarios.pop(i)
            removido = True
            break
    if not removido:
        print("ID inválido.")

# Código principal
def main():
    global id_global
    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar Funcionário")
        print("2. Consultar Funcionário")
        print("3. Remover Funcionário")
        print("4. Encerrar Programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            id_global += 1
            cadastrar_funcionario(id_global)
        elif opcao == "2":
            consultar_funcionarios()
        elif opcao == "3":
            remover_funcionario()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o código principal
if __name__ == "__main__":
    main()
