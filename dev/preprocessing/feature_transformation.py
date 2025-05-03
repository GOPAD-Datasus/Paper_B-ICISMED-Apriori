import numpy as np
import pandas as pd


"""
Unaltered columns: 

- CONSULTAS:
    1: Nenhuma
    2: de 1 a 3
    3: de 4 a 6
    4: 7 e mais
    
- ESTCIVMAE
    1: Solteira
    2: Casada
    3: Viúva
    4: Separado judicialmente/Divorciado

- RACACOR
    1:Branca
    2:Preta
    3:Amarela
    4: Parda
    5: Indígena

- ESCMAE2010
    1: Nenhuma
    2: 1 a 3 anos
    3: 4 a 7 anos
    4: 8 a 11 anos
    5: 12 e mais

- PARTO
    1: Vaginal
    2: Cesáreo
"""


def apgar(df: pd.DataFrame) -> np.array:
    conditions = [
        (df['APGAR5'] <= 5), # 1, 2, 3, 4 e 5
        (df['APGAR5'] <= 7), # 6 e 7
        (df['APGAR5'] >= 8)  # 8, 9 e 10
    ]

    choices = [
        1, # Very bad
        2, # Bad
        3  # Good
    ]

    return np.select(conditions,
                     choices,
                     default=np.nan)


def gestacao(df: pd.DataFrame) -> np.array:
    conditions = [
        (df['GESTACAO'] < 3),  # 1 e 2
        (df['GESTACAO'] < 5),  # 3 e 4
        (df['GESTACAO'] == 5), # 5
        (df['GESTACAO'] == 6)  # 6
    ]

    choices = [
        1, # Pre termo extremo
        2, # Pre termo
        3, # Normal
        4  # Pos termo
    ]

    return np.select(conditions,
                     choices,
                     default=np.nan)


def peso (df: pd.DataFrame) -> np.array:
    conditions = [
        (df['PESO'] < 2500),
        (df['PESO'] < 4000),
        (df['PESO'] >= 4000)
    ]

    choices = [
        1,  # Peso baixo
        2,  # Peso normal
        3   # Peso alto
    ]

    return np.select(conditions,
                     choices,
                     default=np.nan)


def mesprenat (df: pd.DataFrame) -> np.array:
    conditions = [
        (df['MESPRENAT'] <= 3), # 1, 2 e 3
        (df['MESPRENAT'] <= 6), # 4, 5 e 6
        (df['MESPRENAT'] <= 9)  # 7, 8 e 9
    ]

    choices = [
        1,  # Início bom
        2,  # Início ruim
        3   # Início extremamente ruim
    ]

    return np.select(conditions,
                     choices,
                     default=np.nan)


def idademae (df: pd.DataFrame) -> np.array:
    conditions = [
        (df['IDADEMAE'] <= 20), # [  , 20]
        (df['IDADEMAE'] <= 29), # [21, 29]
        (df['IDADEMAE'] <= 35), # [30, 35]
        (df['IDADEMAE'] > 35)   # [36,   ]
    ]

    choices = [
        1,  # Início bom
        2,  # Início ruim
        3,  # Início extremamente ruim
        4
    ]

    return np.select(conditions,
                     choices,
                     default=np.nan)


def codocupmae(df: pd.DataFrame) -> np.array:
    conditions = [
        df['CODOCUPMAE'] == 999992,
        df['CODOCUPMAE'] != 999992
    ]

    choices = [
        1,  # Dona de casa
        2   # Não dona de casa (trabalha)
    ]

    return np.select(conditions,
                     choices,
                     default=np.nan)


def qtdfilvivo (df: pd.DataFrame) -> np.array:
    conditions = [
        (df['QTDFILVIVO'] == 0), # 0
        (df['QTDFILVIVO'] <= 2), # 1 e 2
        (df['QTDFILVIVO'] >= 3)  # 3+
    ]

    choices = [
        0,  # 0 filhos
        1,  # 1 ou 2 filhos
        2   # 3+ filhos
    ]

    return np.select(conditions,
                     choices,
                     default=np.nan)


def qtdfilmort (df: pd.DataFrame) -> np.array:
    conditions = [
        df['QTDFILMORT'] == 0,
        df['QTDFILMORT'] != 0
    ]

    choices = [
        0,  # Nenhum filho morto
        1   # 1+ filho(s) morto(s)
    ]

    return np.select(conditions,
                     choices,
                     default=np.nan)


def codmunnasc(x):
    return int(str(x)[:1])