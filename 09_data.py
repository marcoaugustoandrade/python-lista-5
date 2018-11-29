data = input('Informe a data de nascimento (dd/mm/yyyy): ')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print("%s de %s de %s" % (data[:2], meses[int(data[3:5])], data[-4:]))
