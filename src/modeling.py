import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def train_evaluate_region(df, random_state=12345):
    features = df.drop(columns=["id", "product"])
    target = df["product"]
    features_train, features_valid, target_train, target_valid = train_test_split(
        features, target, test_size=0.25, random_state=random_state
    )
    model = LinearRegression()
    model.fit(features_train, target_train)
    predictions = pd.Series(model.predict(features_valid), index=target_valid.index)
    rmse = mean_squared_error(target_valid, predictions) ** 0.5
    return predictions, target_valid, predictions.mean(), rmse