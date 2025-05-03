import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def encode (file_path: str) -> pd.DataFrame:
    df = pd.read_parquet(file_path)

    encoder = OneHotEncoder(sparse_output=False)
    df_encoded = encoder.fit_transform(df)

    return pd.DataFrame(df_encoded,
                        columns=encoder.get_feature_names_out(),
                        dtype=bool)