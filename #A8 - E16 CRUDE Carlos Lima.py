import pandas as pd
menu = True

ong = [#Cadastra 2 ONGs para facilitar a interação com o Menu
    {
        'CNPJ': '12.345.678/0001-00',
        'nome': 'Energia Sustentavel',
        'endereço': 'Rua Sem Nome, s/n, Sem Bairro'
    },
    {
        'CNPJ': '11.333.888/0001-11',
        'nome': 'Sol Para Todos',
        'endereço': 'Rua Dr. Aqui, s/n, Aculá'
    }
]

cdade = [#Cadastra 5 cdades para facilitar a interação com o Menu
    {
        'nome': 'Comunidade Sol Nascente',
        'endereço': 'Rua das Flores, 123, Zona Rural, Cidade Verde, SP',
        'população': '250',
        'ong responsável': '12.345.678/0001-00'
    },
    {
        'nome': 'Vila Esperança',
        'endereço': 'Avenida Principal, 456, Distrito Água Azul, Campo Claro, MG',
        'população': '500',
        'ong responsável': '12.345.678/0001-00'
    },
    {
        'nome': 'Aldeia Verde',
        'endereço': 'Estrada Velha, s/n, Reserva Florestal, Terra Boa, PR',
        'população': '120',
        'ong responsável': '12.345.678/0001-00'
    },
    {
        'nome': 'Bairro Harmonia',
        'endereço': 'Travessa da Paz, 789, Vila Alegre, Novo Horizonte, RS',
        'população': '300',
        'ong responsável': '12.345.678/0001-00'
    },
    {
        'nome': 'Comunidade São José',
        'endereço': 'Rodovia BR-101, Km 35, Zona Rural, Santa Clara, SC',
        'população': '400',
        'ong responsável': '12.345.678/0001-00'
    }
]

def cadastrarong(): # Cadastra uma nova ONG
    cnpj = input('Informe o CNPJ da ONG a ser cadastrada: ')
    for ong_existente in ong:
        if ong_existente['CNPJ'] == cnpj:
            print('Este CNPJ já está cadastrado. Tente novamente com um CNPJ diferente.')
            return  # Sai da função sem adicionar a ONG
    nome = input('Informe o nome da sua ONG: ')
    endereco = input('Informe o endereço da sua ONG: ')
    # Adiciona os dados na lista ONG
    ong.append({
        'CNPJ': cnpj,
        'nome': nome,
        'endereço': endereco
    })
    print('ONG cadastrada com sucesso!')

def cadastrarcdade(): # Cadastra uma nova comunidade
    nome = input('Informe o nome da sua comunidade: ')
    endereco = input('Informe o endereço de sua comunidade: ')
    populacao = input('Informe cerca de quantos habitantes residem nesta comunidade: ')
    ongresponsavel = input('Informe o CNPJ da ONG de energia sustentável à qual sua comunidade está ligada: ')
    # Adiciona os dados na lista cdade
    cdade.append({
        'nome': nome,
        'endereço': endereco,
        'população': populacao,
        'ong responsável': ongresponsavel
    })
    print("Comunidade cadastrada com sucesso!")
    
def apagarong(): # Apaga uma ONG já cadastrada através do índice
    listarong()  # Mostra a lista de ONGs com os índices
    indice = int(input('Informe o índice da ONG que você gostaria de apagar: '))
    if 0 <= indice < len(ong):
        del ong[indice]
        print(f'ONG no índice {indice} apagada com sucesso.')
    else:
        print('Índice inválido.')

def apagarcdade(): # Apaga uma comunidade já cadastrada através do índice
    listarcdade()  # Mostra a lista de comunidades com os índices
    indice = int(input('Informe o índice da comunidade que você gostaria de apagar: '))
    if 0 <= indice < len(cdade):
        del cdade[indice]
        print(f'Comunidade no índice {indice} apagada com sucesso.')
    else:
        print('Índice inválido.')

def alterarong(): # Altera uma ONG já cadastrada através do índice
    listarong()
    indice = int(input('Informe o índice da ONG que você gostaria de corrigir as informações: '))
    if 0 <= indice < len(ong):
        cnpj = input('Informe o novo CNPJ da ONG: ')
        # Verifica se o CNPJ já está cadastrado
        for i, ong_existente in enumerate(ong):
            if ong_existente['CNPJ'] == cnpj and i != indice:
                print('Este CNPJ já está cadastrado. Tente novamente com um CNPJ diferente.')
                return  # Sai da função sem alterar a ONG
        nome = input('Informe o novo nome da sua ONG: ')
        endereco = input('Informe o novo endereço da sua ONG: ')
      
        ong[indice] = {
            'CNPJ': cnpj,
            'nome': nome,
            'endereço': endereco
        }
        print(f'ONG no índice {indice} alterada com sucesso.')
    else:
        print('Índice inválido.')

def alterarcdade(): # Altera uma comunidade já cadastrada através do índice
    listarcdade()
    indice = int(input('Informe o índice da comunidade que você gostaria de corrigir as informações: '))
    if 0 <= indice < len(cdade):
        nome = input('Informe o novo nome da sua comunidade: ')
        endereco = input('Informe o novo endereço de sua comunidade: ')
        populacao = input('Informe a nova quantidade de habitantes nesta comunidade: ')
        ongresponsavel = input('Informe o novo CNPJ da ONG de energia sustentável à qual sua comunidade está ligada: ')
      
        cdade[indice] = {
            'nome': nome,
            'endereço': endereco,
            'população': populacao,
            'ong responsável': ongresponsavel
        }
        print(f'Comunidade no índice {indice} alterada com sucesso.')
    else:
        print('Índice inválido.')

def listarong(): # Mostra uma tabela das ONGs já cadastradas, para que o índice seja visualizado
    dfo = pd.DataFrame(ong)
    print(dfo)

def listarcdade(): # Mostra uma tabela das comunidades já cadastradas, para que o índice seja visualizado
    df = pd.DataFrame(cdade)
    print(df)

while menu: # Menu do CRUD
    print('Qual operação você gostaria de realizar?')
    print('Digite 1 para adicionar uma ONG')
    print('Digite 2 para remover uma ONG')
    print('Digite 3 para alterar uma ONG já cadastrada')
    print('Digite 4 para ver as ONGs cadastradas')
    print('Digite 5 para adicionar uma comunidade')
    print('Digite 6 para remover uma comunidade')
    print('Digite 7 para alterar uma comunidade já cadastrada')
    print('Digite 8 para ver as comunidades cadastradas')
    print('Digite 9 para sair do programa')
    opcao = int(input('Informe a opção desejada: '))
    
    if opcao == 1:
        cadastrarong()  # Adiciona uma ONG
    elif opcao == 2:
        apagarong()  # Apaga uma ONG já cadastrada
    elif opcao == 3:
        alterarong()  # Altera uma ONG já cadastrada       
    elif opcao == 4:   
        listarong()  # Lista as ONGs em forma de tabela
    elif opcao == 5:
        cadastrarcdade()  # Adiciona uma comunidade
    elif opcao == 6:
        apagarcdade()  # Apaga uma comunidade
    elif opcao == 7:
        alterarcdade()  # Altera uma comunidade       
    elif opcao == 8:   
        listarcdade()  # Lista as comunidades em forma de tabela
    elif opcao == 9:
        menu = False  # Sai do menu
        print('Obrigado por usar o sistema de cadastro de comunidades.')
    else:  # Evita opções erradas para que não saia do menu de forma inesperada
        print('Digite um número de 1 à 9 correspondente à uma das opções.')