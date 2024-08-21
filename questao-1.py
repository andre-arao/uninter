print()
print("Bem-vindos a loja do André Matheus de Paula Arão")
print()

valorDoPedido = float(input("Digite o valor do pedido: "))
quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))
print()

juros = 0

# Regra de juros
if quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 4 / 100

if quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 8 / 100

if quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 13 / 100

if quantidadeParcelas >= 13:
    juros = 32 / 100

# Calculo valorDaParcela
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas

# Calculo valorTotalParcelado
valorTotalParcelado = valorDaParcela * quantidadeParcelas

if quantidadeParcelas >= 4:
    print("Valor das Parcelas:", valorDaParcela)
    print("Valor Total Parcelado:", valorTotalParcelado)

print()

