import pandas as pd


def filter_redundant_rules(file_path: str) -> pd.DataFrame:
    rules = pd.read_csv(file_path)

    filtered_rules = rules.copy()
    rules_to_remove = set()

    for i in range(len(rules)):
        for j in range(i, len(rules)):
            if i != j and \
                    (set(rules.iloc[i]['antecedents'])
                     .issubset(set(rules.iloc[j]['antecedents']))):
                if rules.iloc[i]['confidence'] \
                        <= rules.iloc[j]['confidence']:
                    rules_to_remove.add(i)

    filtered_rules.drop(rules.index[list(rules_to_remove)],
                        inplace=True)

    return filtered_rules

def clear_str(x: str):
    x = x[11:-2]
    table = str.maketrans('', '', "'")
    return x.translate(table)