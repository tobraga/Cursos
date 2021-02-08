# Entrar com dia, mes e ano de aniversario e mostrar formatado

dia = input('Dia que nasceu: ')
mes = input('Mes que nasceu: ')
ano = input('Ano que nasceu: ')

print('Voce nasceu no dia '+ dia +' de '+ mes+ ' de ' + ano +'. Correto?')
print(dia+'/'+mes+'/'+ano)


#melhor forma de fazer
print('Voce nasceu no dia {} de {} de {}. Correto?'.format(dia, mes, ano))

