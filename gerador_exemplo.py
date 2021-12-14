import logging

logging.basicConfig(filename='app.log', 
                    filemode='w',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

import numpy as np
import string
from datetime import datetime, timedelta
import pandas as pd

def _random_choice(charset: np.array):
    return charset[np.random.choice(len(charset), 1)[0]]

def _random_value(charset: np.array, size: int):
    return ''.join([charset[i] for i in np.random.choice(len(charset), size)])

def random_name(size=50):
    return _random_value(string.ascii_uppercase, size)

def random_document(size=15):
    return _random_value(string.digits, size)

def random_document_type(start: int, end: int):
    charset = ['A', 'B', 'C', 'D', 'E', 'F']
    return _random_choice(charset[start:end])

def random_sex():
    return _random_choice(['M', 'F'])

def random_action():
    return _random_choice(['Ignora', 'Atualiza', 'Apaga', 'Adiciona'])

def randon_date():
    return (datetime(year=1970, month=1, day=1) + timedelta(days=np.random.randint(low=0, high=40 * 365))).strftime('%Y-%m-%d')

pessoas = []

for i in range(1000):

    nome = random_name()
    sexo = random_sex()
    nascimento = randon_date()

    documentos = [
        (random_document(), random_document_type(i, i+1))
        for i in range(np.random.randint(low=0, high=3))
    ]
    
    pessoas = pessoas + [(nome, sexo, nascimento, documento, tipo_documento)
                         for documento, tipo_documento in documentos]

arquivo_original = (pd.DataFrame(pessoas, 
                                 columns=['nome', 'sexo', 'nascimento', 'documento', 'tipo_documento'])
                      .drop_duplicates(subset=['nome', 'sexo', 'nascimento', 'tipo_documento']))

pessoas = []

for idx, row in arquivo_original.iterrows():
   
    acao = random_action()

    if acao == 'Apaga':
        logging.info(f'Apagando: {row["nome"]}')
        continue
    elif acao == 'Ignora':
        logging.info(f'Mantém: {row["nome"]}')
        pessoas.append(row)
    elif acao == 'Adiciona':
        logging.info(f'Adiciona: {row["nome"]}')
        pessoas.append(row)
        new_row = row.copy()
        new_row['documento'] = random_document()
        new_row['tipo_documento'] = random_document_type(3,6)
        pessoas.append(new_row)
    elif acao == 'Atualiza':
        logging.info(f'Atualiza: {row["nome"]}')
        new_row = row.copy()
        new_row['documento'] = random_document()
        pessoas.append(new_row)

arquivo_novo = pd.DataFrame(pessoas).drop_duplicates(subset=['nome', 'sexo', 'nascimento', 'tipo_documento'])

arquivo_original.to_csv('arquivo_original.csv')
arquivo_novo.to_csv('arquivo_novo.csv')

