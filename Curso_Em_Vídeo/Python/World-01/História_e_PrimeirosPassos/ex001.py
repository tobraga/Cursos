#Exercicio 01
# Entrar com o nome de uma pessoa, e retornar uma mensagem de boas vindas

nome = input('Qual é o seu nome?')

print('Olá ' + nome + '! Prazer em te conhecer!')

#Melhor forma 

nome2 = input('Qual é o seu nome?')

print('Olá {}! Prazer em te conhecer!'.format(nome2))
