from typing import Tuple
from unittest.mock import inplace

from sklearn.cluster import KMeans
from math import sqrt
from sklearn.preprocessing import MinMaxScaler

from dev.preprocessing.feature_transformation import *


def get_dataframe() -> pd.DataFrame:
    path = '../data/raw/DN2022.parquet.gzip'
    columns = ['APGAR5', 'CONSULTAS', 'GESTACAO', 'PESO',
               'MESPRENAT', 'IDADEMAE', 'ESTCIVMAE',
               'RACACOR', 'ESCMAE2010', 'CODOCUPMAE',
               'CODMUNNASC', 'PARTO', 'QTDFILVIVO',
               'QTDFILMORT', 'TPROBSON']

    return pd.read_parquet(path, columns=columns)


def calculate_wcss(df: pd.DataFrame) -> list:
    wcss = []
    for n in range(2, 11):
        kmeans = KMeans(n_clusters=n, random_state=72)
        kmeans.fit(X=df)
        wcss.append(kmeans.inertia_)

    return wcss


def optimal_number_of_clusters(wcss: list) -> int:
    x1, y1 = 2, wcss[0]
    x2, y2 = 20, wcss[len(wcss) - 1]

    distances = []
    for i in range(len(wcss)):
        x0 = i + 2
        y0 = wcss[i]

        numerator = abs((y2 - y1) * x0 - (x2 - x1)
                        * y0 + x2 * y1 - y2 * x1)
        denominator = sqrt((y2 - y1) ** 2
                           + (x2 - x1) ** 2)
        distances.append(numerator / denominator)

    return distances.index(max(distances)) + 2


def classify_features (df: pd.DataFrame) \
        -> pd.DataFrame:
    df['APGAR5'] = apgar(df)
    df['GESTACAO'] = gestacao(df)
    df['PESO'] = peso(df)
    df['MESPRENAT'] = mesprenat(df)
    df['IDADEMAE'] = idademae(df)
    df['CODOCUPMAE'] = codocupmae(df)
    df['QTDFILVIVO'] = qtdfilvivo(df)
    df['QTDFILMORT'] = qtdfilmort(df)
    df['CODMUNNASC'] = df['CODMUNNASC'].apply(codmunnasc)

    return df


def apply_kmeans(df: pd.DataFrame) \
        -> Tuple[np.array, int]:
    df.drop('TPROBSON', axis=1, inplace=True)

    scaler = MinMaxScaler()
    df = scaler.fit_transform(df)

    n_clusters = optimal_number_of_clusters(
        calculate_wcss(df)
    )

    kmeans = KMeans(n_clusters=n_clusters,
                    random_state=72)
    kmeans.fit_transform(df)

    return kmeans.labels_, n_clusters


def separate_clusters(n_cluster: int,
                      df: pd.DataFrame) -> None:
    preprocessed_path = '../data/preprocessed'

    for i in range(n_cluster):
        temp = df.loc[df['cluster'] == i]
        temp.drop(['cluster'], axis=1, inplace=True)

        temp.to_parquet(preprocessed_path +
                        f'/cluster_{i}.parquet')
