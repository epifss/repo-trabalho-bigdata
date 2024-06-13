import pandas as pd
import numpy as np

notas = pd.read_excel('notas.xlsx')
numNovaLista= 100  
novaLista = pd.DataFrame({
    'Nota': np.round(np.random.uniform(0, 10, numNovaLista), 1),
    'Modalidade': np.random.choice(['Online', 'Presencial'], numNovaLista),
    'Período': np.random.choice(['p2019.2', 'p2020.1', 'p2022.2'], numNovaLista),
    'Disciplina':('Tópicos em LIBRAS,surdez e inclusão'),
    'turno': ('-'),
})
novaLista.to_excel('notas2.xlsx', index=False)
