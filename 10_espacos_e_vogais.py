frase = input('Informe uma frase: ')
print("Há %d espaços em branco na frase informada." % frase.count(' '))

contador = 0
for f in frase:
    if f in 'aeiou':
        contador += 1

print("Aparecem %d vezes as vogais a, e, i, o ou u na frase informada." % contador)
