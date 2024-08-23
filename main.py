import random
import time
import os

def menu():
    print('1 - Acrescentar nome na lista')
    print('2 - Excluir um nome da lista')
    print('3 - Ver nomes na lista')
    print('4 - Sorteio')
    print('5 - Sair do programa')

lista_nomes = []
while True:
    menu()
    
    opcao = input('\nEscolha uma opção: ')
    match opcao:
        
        case '1':
            nome = str(input('Insira um nome a acrescentar: ').capitalize())
            lista_nomes.append(nome)
            print(f'"{nome}" incluído com sucesso')
            print(f'\n Listas de nomes: {lista_nomes}\n')
            continue
        case '2':
            x = -1
            for nome in lista_nomes:
                x += 1    
                print(f'{x} - {nome}')
            print('\nCada número se rerefe o nome o qual se deseja excluir.')
            exclusao = int(input('Digite o número: '))
            del(lista_nomes[exclusao])
            print(f'\nO nome {lista_nomes[exclusao]} foi excluído com sucesso\n')
            continue
        
        case '3':
            x = -1
            for nome in lista_nomes:
                x += 1    
                print(f'{x} - {nome}')
            print('\n')
            continue

        case '4':
            print('Sorteando em...')
            time.sleep(1)
            os.system('cls')
            print('3')
            time.sleep(1)
            os.system('cls')
            print('2')
            time.sleep(1)
            os.system('cls')
            print('1')
            time.sleep(1)
            os.system('cls')
            print('...')
            time.sleep(1)
            os.system('cls')
            sorteado = random.choice(lista_nomes)
            print(f'\nO nome sorteado foi... {sorteado}\n')
            print(f'PARABÉNS {nome}')
            continue
        
        case '5':
            print('Saindo do pragrama...')
            time.sleep(2)
            os.system('cls')
            break
        case _:
            print('Opção inválida')
            continue


