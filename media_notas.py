nome_aluno = input('Digite seu nome completo: ')
bimestre_1 = float(input('Primeiro bimestre: '))
bimestre_2 = float(input('Segundo bimestre: '))
bimestre_3 = float(input('Terceiro bimestre: '))
bimestre_4 = float(input('Quarto bimestre: '))
media_final = (bimestre_1 + bimestre_2 + bimestre_3 + bimestre_4) / 4

print('Olá {}'.format(nome_aluno), '! \nsua média final é: {}'.format(media_final))
if media_final >= 7:
    print('Parabéns!! \nVocê passou de ano')
else:
    print('Você foi reprovado. \nEstude mais no próximo ano')