import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

mlflow.set_tracking_uri('http://localhost:5000')
mlflow.autolog()

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

model = RandomForestClassifier(n_estimators=10, max_depth=1, max_features=6)
model.fit(X_train, y_train)

with mlflow.start_run():
    mlflow.sklearn.log_model(model, "model")

    mlflow.register_model(
        "runs:/" + mlflow.active_run().info.run_id + "/model",
        "IrisModel"
    )
