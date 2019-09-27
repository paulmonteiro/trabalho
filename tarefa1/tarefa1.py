import random
# cria uma lista de 10 pontuacoes compreendidas entre 0 e 20, de forma aleatoria:
lista_pontuacoes = [random.randint(0,20) for i in range(10)]

print(f'Lista de pontuações: {lista_pontuacoes}')

# metodo para encontrar a pontuaçao mais elevada:
def encontra_maior(pontuacoes) :
    # copia da lista original para se poder ordenar sem alterar a original
    pontuacoes = pontuacoes[:]
    # ordena a lista:
    pontuacoes.sort(reverse=True)
    # devolve a pontuação mais elevada:
    return(pontuacoes[0])

def remove_duplicados(lista_com_duplicados) :
    # convertendo para set ficamos sem duplicados
    # em seguida converte novamente para lista para se poder fazer slices
    lista_sem_duplicados = list(set(lista_com_duplicados))
    return lista_sem_duplicados

# encontrar as tres pontuaçoes mais elevadas:
def encontra_tres_maiores(pontuacoes) :
    pontuacoes = remove_duplicados(pontuacoes)
    # copia da lista original para se poder ordenar sem alterar a original
    pontuacoes = pontuacoes[:]
    pontuacoes.sort(reverse=True)
    return pontuacoes[0:3]

maior_pontuacao = encontra_maior(lista_pontuacoes)
print(f'Maior pontuação: {maior_pontuacao}')

tres_mais_elevadadas = encontra_tres_maiores(lista_pontuacoes)
# converte a list para string:
tres_mais_elevadadas = ', '.join(str(x) for x in tres_mais_elevadadas)
print(f'As três pontuações mais elevadas são: {tres_mais_elevadadas}')

ultima_adicionada = lista_pontuacoes[-1]
print(f'A ultima pontuação a ser adicionada a lista foi: {ultima_adicionada}')
