string1 = input('Informe o conteúdo da primeira string: ')
string2 = input('Informe o conteúdo da segunda string: ')

print("String 1: %s" % string1)
print("String 2: %s" % string2)
print("Tamanho de %s: %d " % (string1, len(string1)))
print("Tamanho de %s: %d " % (string2, len(string2)))

if len(string1) != len(string2):
    print("As strings possuem tamanho diferente!")
    print("As strings possuem conteúdo diferente!")
else:
    print("As strings possuem o mesmo tamanho!")
    conteudo = True
    for i in range(0, len(string1)):
        if string1[i] != string2[i]:
            conteudo = False
            break
    if conteudo:
        print("As strings possuem o mesmo conteúdo!")
    else:
        print("As strings possuem conteúdo diferente!")
