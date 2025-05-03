import pandas as pd

from dev.apriori.apriori import apply_apriori
from dev.postprocessing.postprocess import postprocess
from dev.preprocessing.preprocess import preprocess


if __name__ == '__main__':
    pd.options.mode.copy_on_write = True

    n_cluster = preprocess()
    apply_apriori(n_cluster)
    postprocess(n_cluster)