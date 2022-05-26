
# D


from time import sleep
from tracemalloc import stop

def MenuMessage(): # Função de exibição do menu
    print('1 - Cadastrar uma série de TV'
    '\n2 - Consultar informações de uma série'
    '\n3 - Gerar listagem das séries registradas'   
    '\n9 - Sair')

def QuitProgram(userEntry): # Função para encerrar o programa.
    if userEntry == 9:
        print('Programa encerrado.')
        quit()

def TotalDeEp(list, userSerieChoise):
    # Essa função percorre toda a lista comparando a entrada do usuário com o os elementos presentes nela.
    # Quando o elemento é encontrado, a função retorna o próximo elemento da lista, pois, o nome da série e
    # as informações da mesma são armazenadas na mesma sequência, sempre. Primeiro é o nome da série, em se-
    # guida é a quantidade de total de episódios e por fim, o ultimo episódio assistido.
    for i in range(len(list)):
        if list[i] == userSerieChoise:
            return list[i + 1]

def UtimoEp(list, userSerieChoise):
    # Essa função faz o mesmo que a anterior, mas aqui ela pula dois elementos.
    # Ao fazer isso, o valor a ser retornado será o ultimo episódio assistido, 
    # pois essas três informações são armazenadas sempre na mesma sequência.
    for i in range(len(list)):
        if list[i] == userSerieChoise:
            return list[i + 2]

def OptionError(userChoise):
    print(f'ERRO DE EXECUÇÃO. A opção {userChoise} não existe.')
    print('Programa encerrado.')
    quit()



# Main method
print('\nGerenciador de Séries de TV'
'\n------------------------------------\n')

MenuMessage() # Função do menu.

userEntry = int(input('\nSua escolha: '))
print('')

QuitProgram(userEntry) # Fecha o programa caso o usuário deseje.


allSeries = [] # Array onde serão armazenadas as informações.

while userEntry != 0:
    
    # Variável para exeutar o While.
    execute = True 
    
    match userEntry: # Match Case para execução de acordo com a escolha feita no menu
        
        case 1: # Essa opção está fucinando e armazendo as séries corretamente

            # Nessa opção, o programa vai registrar as séries que o usuário dejesa.
            
            # As informações serão armazenadas em uma lista, sempre na mesma sequência,
            # primeiro é o nome da série, em seguida o total de episódios e o ultimo
            # episódio assistido.

            # Foi tentado, em uma vez anterior desse código, gerar várias listas que seriam
            # armazenadas em uma única lista. Cada lista dentro dessa lista principal, seria
            # uma série, mas foi visto que não foi encontrada uma maneira de acessar o con-
            # teúdo de cada série. A solução foi armazenar tudo junto, em uma única lista.

            while execute == True: 
            
                serieName = input('Nome da série: ').upper()
                epTotal = int(input('Quantidade total de episódios: '))
                lastOneWatched = int(input('Ultimo episódio assistido: '))

                if lastOneWatched > epTotal:
                    print('\nNão é possível fazer o cadastro pois o número do ultimo episódio assistido '
                    'é maior que o total de episódios.\n'
                    'Você será redirecionado ao menu em instantes.\n')
                    sleep(10)
                    break

                allSeries.append(serieName)
                allSeries.append(epTotal)
                allSeries.append(lastOneWatched)

                print(f'\nA série {serieName} foi registrada com sucesso.')

                print('\nO que deseja fazer?\n\n'
                'Cadastrar - Cadastra um nova série.\n'
                'Voltar - Retorna ao menu.')
                userChoise = input('Sua escolha: ').upper()
                print('')
    
                if userChoise == 'CADASTRAR':
                    execute = True
                elif userChoise == 'VOLTAR':
                    execute = False
                else:
                    OptionError(userChoise)

        case 2: # Está funcionando corretamente, atendendo todas as exigência.
            
            # Nessa opção, o programa pergunta ao usuário o nome de uma série para consultar as informações.
            # Aqui também, caso nenhuma série tenha sido cadastrada, o programa informará o que ocorreu e retornará ao menu.

            # Será feita uma checagem e se a série informada pelo usuário esteja cadastrada, será exibida as informações da 
            # mesma, caso não esteja, o programa irá informar ao usuário de que a série não foi encontrada.

            # Ao final, depois que a consulta ter sido feita, o programa perguntará ao usuário o que ele deseja fazer. Serão
            # duas opções, fazer uma nova consulta e retornar ao menu.
            
            while execute == True:
                
                if len(allSeries) == 0:
                    print('Nunhuma série foi cadastrada. Faça o cadrasto para ter acesso as informações.\n') 
                    break
                
                userSerieChoise = input('Informe nome da série para consulta: ').upper()

                if userSerieChoise in allSeries: # checa se a séria está registrada

                    totalEpisodes = TotalDeEp(allSeries, userSerieChoise)
                    lastEpisodesWatched = UtimoEp(allSeries, userSerieChoise)
                    
                    percentageWatched = (lastEpisodesWatched / totalEpisodes) * 100

                    print(f'\nA série {userSerieChoise} foi encontrada.\n'
                    f'Quantidade de episódio: {totalEpisodes}\nUltimo episódio assistido: {lastEpisodesWatched}\n'
                    'Percentual concluído: {:.1f}%\n'.format(percentageWatched))
                    
                else: # Informa que a digitada não foi encontrada
                    print(f'A série {userSerieChoise} não foi encontrada. Faça o cadastro para acessar mais informações.\n')
                    

                print('O que deseja fazer?\n\n'
                'Consultar - Consultar uma nova série.\n'
                'Voltar - Retorna ao menu.')
                userChoise = input('Sua escolha: ').upper()
                print('')

                if userChoise == 'CONSULTAR':
                    execute = True
                elif userChoise == 'VOLTAR':
                    execute = False
                else:
                    OptionError(userChoise)
        
        case 3: 
            while execute == True:
            
                if len(allSeries) == 0:
                        print('Nunhuma série foi cadastrada. Faça o cadrasto para ter acesso as informações.\n')
                        break

                print('\nEm instantes a lista com todas as séries cadastradas será exibida.')
                sleep(3)

                episodios = 0
                assistido = 0
                percentualTotal = 0
                cont = 0 

                for i in range (0, len(allSeries), 3):

                    serieName1 = allSeries[i]
                    totalEpisodes1 = allSeries[i + 1]
                    ultimoAssistido1 = allSeries[i + 2]
                    percentualSeparado = (ultimoAssistido1 / totalEpisodes1) * 100
                    
                    print('')
                    print(f'Nome da série: {serieName1}')
                    print(f'Total de episódios: {totalEpisodes1}')
                    print(f'Ultimo episódio assistido: {ultimoAssistido1}')
                    print(f'Percentual concluído: {percentualSeparado:.1f}%')

                    episodios += totalEpisodes1
                    assistido += ultimoAssistido1
                    cont += 1


                percentualTotal = (assistido / episodios) * 100

                if len(allSeries) == 3:
                    print(f'\nPercentua geral concluído: {percentualTotal:.1f}%')
                    print(f'Você tem cadastrada apenas {cont} série cadastrada.')
                    print('\nVocê será redirecionado ao menu em instantes.\n')
                elif len(allSeries) > 3:
                    print(f'\nPercentua geral concluído: {percentualTotal:.1f}%') 
                    print(f'Você tem um total de {cont} séries cadastradas.')
                    print('\nVocê será redirecionado ao menu em instantes.\n')
                sleep(3)
                
                execute = False # Encerra a execução da listagem e retorna ao menu.
                
        case 9: # Encerra a execução do programa.

            # Ao selecionar essa opção, o programa chama uma função criar para encerrar o programa

            QuitProgram(userEntry)

    MenuMessage() # Exibe o menu novamente.
    userEntry = int(input('\nSua escolha: '))
    print('')



