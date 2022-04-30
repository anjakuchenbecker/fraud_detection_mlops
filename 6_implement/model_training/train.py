# TODO: develop training module

# External imports
import mlflow
import argparse
import os
# Internal imports
# NA


def setup():
    """
    Setup the training module
    """

    # Retrieve environment variables
    MLFLOW_TRACKING_SERVER_URL = os.environ.get("MLFLOW_TRACKING_SERVER_URL")

    # Setup the command-line parser
    parser = argparse.ArgumentParser()
    parser.add_argument("mlflow_run_id",
                        help="Set the MLflow run id",
                        type=str)
    args = parser.parse_args()

    # Set tracking uri (tracking server and registry server are the same / not separated)
    # No need to set the registry uri in addition, because it defaults to the tracking URI
    mlflow.set_tracking_uri(MLFLOW_TRACKING_SERVER_URL)
    return str(args.mlflow_run_id)


def load_processed_data():
    """
    TODO
    """

    # TODO processed_train.<file>, processed_test.<file>
    # return train_X, train_y, test_X, test_y
    pass


def calculate_eval_metrics(actual, predicted):
    """
    TODO
    """

    # TODO
    # Mean squared error regression loss
    # rmse = mean_squared_error(y_true=actual, y_pred=predicted, squared=False)
    # Mean absolute error regression loss
    # mae = mean_absolute_error(actual, predicted)
    # r2 = r2_score(actual, predicted)
    # return rmse, mae, r2
    pass


def train(mlflow_run_id):
    """
    TODO
    """

    # train_X, train_y, test_X, test_y
    model_params = {"Pa_Dummy_1": 1, "Pa_Dummy_2": 2}
    # model_name = "TBD"

    with mlflow.start_run(run_id=mlflow_run_id) as run:
        # define and fit model with params on processed training dataset
        # TODO .fit(train_X, train_y)

        # predict on processed test dataset
        # TODO predicted = (test_X)

        # calculate evaluation metrics
        # TODO eval_metrics(test_y, predicted)

        # log experiment
        mlflow.log_params(model_params)
        # mlflow.log_metrics("TBD", TBD)
        # mlflow.log_artifacts("TBD", TBD)
        # mlflow.sklearn.log_model("TBD", TBD)


if __name__ == "__main__":
    mlflow_run_id = setup()
    train(mlflow_run_id)
    print("xxx")