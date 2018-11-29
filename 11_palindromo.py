frase = input('Informe a frase: ')
frase = frase.replace(" ", "").upper()

nova_frase = ''

for i in range(len(frase) - 1, -1, -1):
    nova_frase += frase[i]

if nova_frase == frase:
    print("A frase informada é um palíndromo!")
else:
    print("A frase informada não é um palíndromo")
