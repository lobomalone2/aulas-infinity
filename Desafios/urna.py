candidatos = {
    'A': {'votos': 0 },
    'B': {'votos': 0 },
    'C': {'votos': 0 }
}


print(candidatos)
voto = ''
print('Candidatos disponíveis: ')

for cand in candidatos.keys():
    print(f'Candidato: {cand}')


while True:
    
    voto = input('Digite um candidato pra votar')

       
    if voto == 'sair':
        print('Encerrando votação')
        break

    elif voto not in candidatos:
        print('Candidato não encontrado tente novamente!')
        continue

    candidatos[voto]['votos'] += 1


for cand, votos in candidatos.items():
    memoria = []

    for valor in votos.values():

        memoria.append(valor)


    print(f'Candidato {cand} - votos: {memoria[0]} ')

if candidatos['A']['votos'] > candidatos['B']['votos'] and candidatos['A']['votos'] > candidatos['C']['votos']:

    print('O candidato A Venceu')

elif candidatos['B']['votos'] > candidatos['A']['votos'] and candidatos['B']['votos'] > candidatos['C']['votos']:

    print(' O candidato B Venceu!')

elif candidatos['C']['votos'] > candidatos['B']['votos'] and candidatos['C']['votos'] > candidatos['A']['votos']:

    print('O Candidato C venceu!')


total = candidatos['A']['votos'] + candidatos['B']['votos'] + candidatos['C']['votos']


for cand, votos in candidatos.items():
    
    try:
        percentual = float((votos['votos'] /total)) * 100

    except ZeroDivisionError:

        print('')
        percentual = 0

    print(f'Candidato A {cand} -  {percentual:.2f} % ')

        







# Pesquisar uma biblioteca em python que gera um PDF com base em relatórios

    


















