from dev.apriori.utils import encode
from mlxtend.frequent_patterns import apriori, association_rules


def apply_apriori (n_cluster: int):
    file_list = [f'../data/preprocessed/cluster_{i}.parquet'
                 for i in range(n_cluster) ]

    for file, i in zip(file_list, range(n_cluster)):
        df_encoded = encode(file)

        freq_items = apriori(df_encoded,
                             min_support=0.6,
                             use_colnames=True)

        rules = association_rules(freq_items,
                                  metric='confidence',
                                  min_threshold=0.9,
                                  num_itemsets=4)
        rules = rules.sort_values(['confidence'],
                                  ascending=[False])

        path = f'../data/intermediate/rules_{i}.csv'
        rules.to_csv(path, index=False)
