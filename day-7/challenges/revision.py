import random
lista_de_palavras = [
    "carro",
    "moto",
    "computador"
]
escolha_de_palavra = random.choice(lista_de_palavras)


print(f"A palavra sorteada foi: {escolha_de_palavra}")
display = []
tamanho_da_palavra = len(escolha_de_palavra)

for _ in range(tamanho_da_palavra):
    display += "_"
print(display)

fim_de_jogo = False
while not fim_de_jogo:
    advinhar_letra = input("Escolha uma letra: ").lower()

    for posicao in range(tamanho_da_palavra):
        letra = escolha_de_palavra[posicao]
        if letra == advinhar_letra:
            display[posicao] = letra
    if "_" not in display:
        fim_de_jogo = True
        print("O Jogo acabou!")
    print(display)

# for letra in escolha_de_palavra:
#     if letra == advinhar_letra:
#         print("Acertou")
#     else:
#         print("Errou")
# print(escolha_de_palavra)
