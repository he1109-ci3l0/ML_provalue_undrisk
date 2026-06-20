import numpy as np
import pandas as pd
from .profit import profit, BUDGET, N_WELLS

N_STUDIED = 500


def bootstrap_profit(target, predictions, n_samples=1000, n_studied=N_STUDIED,
                     n_wells=N_WELLS, revenue_per_unit=4500, random_state=12345):
    state = np.random.RandomState(random_state)
    target = target.reset_index(drop=True)
    predictions = predictions.reset_index(drop=True)
    profits = []
    for _ in range(n_samples):
        positions = state.choice(len(target), size=n_studied, replace=True)
        sample_target = target.iloc[positions].reset_index(drop=True)
        sample_pred = predictions.iloc[positions].reset_index(drop=True)
        profits.append(profit(sample_target, sample_pred, n_wells, revenue_per_unit))
    return pd.Series(profits)