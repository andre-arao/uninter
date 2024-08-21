# Meu RU
RU=4916426

print()
print('''Bem-vindos a loja de Marmitas do André Matheus de Paula Arão RU: ''', RU)
print()
print(
''' ****************Cardápio******************
| Tamanho |          Descrição         | Valor |
|   P     |       Bife Acebolado       | 16,00 |
|   M     |       Bife Acebolado       | 18,00 |
|   G     |       Bife Acebolado       | 22,00 |
|   P     |       Filé de Frango       | 15,00 |
|   M     |       Filé de Frango       | 17,00 |
|   G     |       Filé de Frango       | 21,00 |''')
print()

# Acumulador para o valor total
valor_total = 0

while True:
    # Input do sabor
    sabor = input("Digite o sabor (BA para Bife Acebolado, FF para Filé de Frango): ").upper()
    
    if sabor not in ["BA", "FF"]:
        print("Sabor inválido. Tente novamente.")
        print()
        continue

    # Input do tamanho
    tamanho = input("Digite o tamanho (P/M/G): ").upper()
    print()

    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        print()
        continue

    # Definindo o preço com base no sabor e tamanho
    if sabor == "BA":
        if tamanho == "P":
            preco = 16.00
        elif tamanho == "M":
            preco = 18.00
        elif tamanho == "G":
            preco = 22.00
    elif sabor == "FF":
        if tamanho == "P":
            preco = 15.00
        elif tamanho == "M":
            preco = 17.00
        elif tamanho == "G":
            preco = 21.00

    # Adiciona o preço ao valor total
    valor_total += preco

    # Pergunta se o usuário deseja continuar
    mais = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    print()
    
    if mais == "N":
        break

# Exibe o valor total do pedido
print()
print(f"\nO valor total do seu pedido é: R$ {valor_total:.2f}")
