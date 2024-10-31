from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table
import os



def criarpdf(dados):
    
    # Criar o canvas
    caminho = os.path.join(os.getcwd(),'Resultado_votação.pdf')

    c = canvas.Canvas('Resultado_votação.pdf', pagesize=A4)
    c.setFont('Helvetica', 12)
    c.drawString(100,750,'Resultado da votação!!')
    c.setFont('Helvetica-Bold', 12)
    c.save() # Salvar o canvas antes de criar o SimpleDocTemplate

    # Preparar os dados da tabela
    data = [['NOME','VOTOS']]

    for nome, votos in dados.items():

        data.append([nome,votos]) 

    # Criar o documento PDF

    pdf = SimpleDocTemplate('Resultado_votação.pdf', pagesize=A4)
    tabela = Table(data)

     # Construir o PDF com a tabela

    pdf.build([tabela])

    print(f'O pdf foi salvo em: {caminho}')

                                                                                                                    
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

    print(f'Candidato {cand} -  {percentual:.2f} % ')


criarpdf(candidatos)

        







# Pesquisar uma biblioteca em python que gera um PDF com base em relatórios

    


















