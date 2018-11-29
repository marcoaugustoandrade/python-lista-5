nome = input('Informe o seu nome (maiúsculas e minúsculas): ')
for i in range(len(nome) - 1, -1, -1):
    print(nome[i].upper(), end = "")
