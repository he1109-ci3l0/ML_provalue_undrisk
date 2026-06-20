BUDGET = 100_000_000
N_WELLS = 200
REVENUE_PER_UNIT = 4500


def profit(target, predictions, n_wells=N_WELLS, revenue_per_unit=REVENUE_PER_UNIT, budget=BUDGET):
    top_indices = predictions.sort_values(ascending=False).index[:n_wells]
    selected_volume = target.loc[top_indices].sum()
    return selected_volume * revenue_per_unit - budget