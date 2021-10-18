# Importando time para atribuir atrasos entre linhas de código
from time import sleep

print("----------------------------------", "\n")

# Criando lista de números aleatórios 
numbers = [1, 34, 53, 21, 10, 67, 81, 135, 543]
# Imprimindo a lista
print("Lista criada com sucesso!")
# Atrasando o código em 2 segundos
sleep(2)
# Imprimindo lista
print("\n", "Lista: ", numbers, '\n')
# Atrasando o código em 1 segundo
sleep(1)
# Imprimindo maior valor da lista
print('O maior valor desta lista é: ', max(numbers), "\n")
# Atrasando o código em 2 segundos
sleep(2)
# Imprimindo menor valor da lista
print('O menor valor desta lista é: ', min(numbers), "\n")
# Adicionando um item a lista
numbers.append(222)
# Atrasando o código em 2 segundos
sleep(2)
#Mensagem de atualização
print('-----------------------------------------', '\n')
# Atrasando o código em 1 segundo
sleep(1)
# Imprimindo mensagem de atualização da lista
print('Lista de números atualizada!', '\n')
# Atrasando o código em 2 segundos
sleep(1)
# Imprimindo nova lista
print(numbers, '\n')