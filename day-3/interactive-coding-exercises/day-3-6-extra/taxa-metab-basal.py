# A fórmula da tmb é baseada na equação de Harry Benedict

genero = input("Qual o seu gênero? M ou F: ")
peso = float(input("Qual o seu peso em Kg? "))
altura = float(input("Qual a sua altura em cm? "))
idade = int(input("Qual a sua idade? "))

if genero == 'M' or genero == 'm':
    tmb = round(66.47 + (13.75 * peso) + (5.003 * altura) - (6.775 * idade), 2)
    print(f"Sua taxa de metabolismo basal é de {tmb} cal")
elif genero == 'F' or genero == 'f':
    tmb = round(655.09 + (9.563 * peso) + (1.85 * altura) - (4.676 * idade), 2)
    print(f"Sua taxa de metabolismo basal é de {tmb} cal")