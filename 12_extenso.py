unidade = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dezena2 = ['onze', 'doze', 'treze', 'quatorze', 'quinze', 'dessesseis', 'dessete', 'dezoito', 'dezenove']
dezena = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

numero = int(input('Informe um número entre 0 e 99: '))

if numero < 10:
    print(unidade[numero])
elif numero >= 10 and numero < 20:
    print("%s" % dezena2[int((numero - (numero % 10)) / 10) - 1])
else:
    if numero % 10 == 0:
        print("%s" % (dezena[int((numero - (numero % 10)) / 10) - 1]))
    else:
        print("%s e %s" % (dezena[int((numero - (numero % 10)) / 10) - 1], unidade[numero % 10]))
