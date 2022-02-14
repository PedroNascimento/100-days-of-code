"""
    Challenge - Day 1: Working with Variables in Python to Manage Data

    A proposta desse desafio é implementar um algoritmo que gere nome para uma Banda Musical.
    1) Deve informar o nome da cidade onde cresceu;
    2) O nome do seu primeiro aninal de estimação.
    3) Imprimir o nome da Banda usando as duas informações acima
"""
print("Bem vindos ao gerador de nomes de Bandas")
nameCity = input("Qual o nome da Cidade que você cresceu?\n")
namePet = input("Qual o nome de seu animal de estimação?\n")

print(f"O nome de sua Banda será {nameCity} {namePet}")