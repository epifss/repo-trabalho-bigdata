
import pandas as pd
notas= pd.read_excel('notas.xlsx')
notas2= pd.read_excel('notasB.xlsx')
alunos = pd.concat([notas, notas2], ignore_index=True)
alunos['aluno'] = [f'aluno {i+1}' for i in range(len(alunos))]
ordem_colunas = ['aluno'] + [col for col in alunos.columns if col != 'aluno']
alunos = alunos[ordem_colunas]
alunos['Período'] = 'p' + alunos['Período'].astype(str)
alunos= alunos.drop(columns=['Disciplina','Turno'])
alunos.to_excel('alunos.xlsx', index=False)

online2019=alunos.query('Modalidade=="Online"').query('Período=="p2019.2"')
online2020=alunos.query('Modalidade=="Online"').query('Período=="p2020.2"')
online2022=alunos.query('Modalidade=="Online"').query('Período=="p2022.1"')
presencial2019=alunos.query('Modalidade=="Presencial"').query('Período=="p2019.2"')
presencial2022=alunos.query('Modalidade=="Presencial"').query('Período=="p2022.1"')
online=alunos.query('Modalidade=="Online"')

presencial=alunos.query('Modalidade=="Presencial"')
online2019.to_excel('online2019.xlsx', index=False)
online2020.to_excel('online2020.xlsx', index=False)
online2022.to_excel('online2022.xlsx', index=False)
presencial2019.to_excel('presencial2019.xlsx', index=False)
presencial2022.to_excel('presencial2022.xlsx', index=False)
online.to_excel('online.xlsx',index=False)
presencial.to_excel('presencial.xlsx',index=False)
