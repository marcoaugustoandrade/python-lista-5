string = input('Informe um string: ')
print("Tamanho da string utilizando o método len: %d" % len(string))

contador = 0
for s in string:
    contador += 1

print("Tamanho da string sem o método len: %d" % contador)
