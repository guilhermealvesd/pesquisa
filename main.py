#Lista de nomes

nomes = ['Guilherme', 'Matheus', 'Douglas', 'João', 'Felipe', 'Renato', 'Carlos', 'Amanda', 'Eliane', 'Júlia', 'Débora', 'Fernanda', 'Regina', 'Angelina', 'Cristiane']

#Usuário informa o nome que deseja pesquisar

nome = input('Digite o nome a ser pesquisado: ').capitalize()

#Verifica se o nome está na lista ou não
try:
    #Retorna o índice do nome pesquisado
    indice = nomes.index(nome)
    print(f' Nome encontrado: {nome} no índice {indice}.')     
except:
    print(f'{nome} não encontrado na lista.')