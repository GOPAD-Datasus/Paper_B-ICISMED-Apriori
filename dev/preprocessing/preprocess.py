from dev.preprocessing.utils import *


def preprocess() -> int:
    df_apriori = get_dataframe()

    df_apriori.dropna(inplace=True)

    df_apriori['cluster'], n_clusters = \
        apply_kmeans(df_apriori)

    df_apriori = classify_features(df_apriori)

    separate_clusters(n_clusters, df_apriori)

    return n_clusters