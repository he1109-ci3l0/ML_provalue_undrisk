import pandas as pd


def load_regions(raw_dir="data/raw"):
    files = {
        "Región 0": f"{raw_dir}/geo_data_0.csv",
        "Región 1": f"{raw_dir}/geo_data_1.csv",
        "Región 2": f"{raw_dir}/geo_data_2.csv",
    }
    return {name: pd.read_csv(path) for name, path in files.items()}