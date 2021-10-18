# Simulação de validação de usuário

# importando time para atribuir atrasos entre linhas de código
from time import sleep

# Pegando dados usuário
print('\n' + '--------- Captando dados e validando entrada ---------------' + '\n')
# Atrasando o código em 1 segundo
sleep(1)
# Armazenando dado do input
name = input('\n' + 'Digite seu nome: ' + '\n')
# Atrasando o código em 1 segundo
sleep(1)
# Valor setor
setor = 'Ciencia de Dados'
# Armazenando dado do input para análise
setorInput = input('\n' + 'Digite seu setor: ' + '\n')
# Atrasando o código em 1 segundo
sleep(1)
print('\n' + 'Analisando dados...')
# Atrasando o código em 2 segundos
sleep(2)
# Armazenando dado do input para análise
code = '2w9kggw5'
codeInput = input('\n' + 'Digite seu código: ' + '\n')
# Atrasando o código em 1 segundo
sleep(1)

# Estrutura de condição composta para validar código
if ((setorInput == setor) & (codeInput == code)):
    print('\n' + 'Verificando código, aguarde um momento...' + '\n')
    # Atrasando o código em 2 segundos
    sleep(2)
    # Imprimindo mensagem de sucesso
    print('\n' + 'Hey' + ' ' + name + '!' +
          ' ' + 'Verificado, entrada liberada.')
    # Atrasando o código em 2 segundos
    sleep(2)
    # Imprimindo mensagem de encerramento
    print('\n' + 'Atendimento encerrado' + '\n')
else:
    print('\n' + 'Verificando código, aguarde um momento...' + '\n')
    # Atrasando o código em 3 segundos
    sleep(3)
    # Mensagem de erro
    print('\n' + 'Código inválido!')
    # Atrasando código em 3 segundos
    sleep(3)
    # Imprimindo mensagem de encerramento
    print('\n' + 'Atendimento encerrado' + '\n')
