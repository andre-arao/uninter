print()
print("Bem-vindos à Fábrica de Camisetas do André Matheus de Paula Arão")
print()

# Função para escolher o modelo
def escolha_modelo():
    modelos = {
        'MCS': 1.80,
        'MLS': 2.10,
        'MCE': 2.90,
        'MLE': 3.20
    }
    while True:
        modelo = input("Escolha o modelo (MCS - Manga Curta Simples / MLS - Manga Longa Simples / MCE - Manga Curta Com Estampa / MLE - Manga Longa Com Estampa): ").upper()
        if modelo in modelos:
            return modelos[modelo]
        else:
            print("Modelo inválido. Tente novamente.")

# Função para informar o número de camisetas
def num_camisetas():
    while True:
        try:
            quantidade = int(input("Digite o número de camisetas: "))
            if quantidade > 20000:
                print("Quantidade de camisetas acima do limite. Tente novamente.")
                continue
            if quantidade >= 2000:
                desconto = 0.12
            elif quantidade >= 200:
                desconto = 0.07
            elif quantidade >= 20:
                desconto = 0.05
            else:
                desconto = 0
            return quantidade, desconto
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Função para escolher o tipo de frete
def frete():
    while True:
        try:
            tipo_frete = int(input("Escolha o tipo de frete (0: retirar na fábrica, 1: transportadora, 2: Sedex): "))
            if tipo_frete == 0:
                return 0
            elif tipo_frete == 1:
                return 100
            elif tipo_frete == 2:
                return 200
            else:
                print("Opção de frete inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite 0, 1 ou 2.")

# Código principal
def main():
    modelo_valor = escolha_modelo()
    quantidade, desconto = num_camisetas()
    valor_camisetas = modelo_valor * quantidade
    valor_desconto = valor_camisetas * desconto
    valor_final = valor_camisetas - valor_desconto
    valor_frete = frete()
    total_pagar = valor_final + valor_frete
    
    print(f"\nResumo do Pedido:")
    print(f"Modelo escolhido: R$ {modelo_valor:.2f}")
    print(f"Número de camisetas: {quantidade}")
    print(f"Desconto aplicado: {desconto * 100}%")
    print(f"Valor total sem frete: R$ {valor_camisetas - valor_desconto:.2f}")
    print(f"Valor do frete: R$ {valor_frete:.2f}")
    print(f"Total a pagar: R$ {total_pagar:.2f}")

# Executa o código principal
if __name__ == "__main__":
    main()
