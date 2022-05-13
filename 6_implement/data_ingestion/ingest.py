# TODO: develop ingestion module

# External imports
import mlflow
import os
# Internal imports
# NA


def setup():
    """
    Setup the ingestion module
    """

    # Retrieve environment variables
    MLFLOW_TRACKING_SERVER_URL = os.environ.get("MLFLOW_TRACKING_SERVER_URL")
    MLFLOW_EXPERIMENT_NAME = os.environ.get("MLFLOW_EXPERIMENT_NAME")

    # Set tracking uri (tracking server and registry server are the same / not separated)
    # No need to set the registry uri in addition, because it defaults to the tracking URI
    mlflow.set_tracking_uri(MLFLOW_TRACKING_SERVER_URL)
     # Set experiment
    mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)

    # Create output directory for data
    path_to_data = "output/data"
    os.makedirs(path_to_data, exist_ok=True)
    return path_to_data


def load_raw_data(path_to_data):
    """
    TODO
    """

    # TODO Load raw data from data source
    raw_data = "raw_data_dummy"

    # TODO Save to raw_data.<file>
    with open(f"{path_to_data}/raw_data.txt", 'w') as f:
        f.write(raw_data)


def split_raw_data(path_to_data):
    """
    TODO
    """

    # TODO Split raw data to train and test dataset
    raw_data_train = "raw_data_train_dummy"
    raw_data_test = "raw_data_test_dummy"

    # TODO Save to raw_train.<file> and raw_test.<file>
    with open(f"{path_to_data}/raw_train.txt", 'w') as f:
        f.write(raw_data_train)
    with open(f"{path_to_data}/raw_test.txt", 'w') as f:
        f.write(raw_data_test)

    pass


def log_raw_data(path_to_data):
    """
    TODO
    """

    # Start a new run, as we are in the first step in our pipeline
    # TODO add run name
    with mlflow.start_run() as run:
        # TBD
        mlflow.log_artifacts(path_to_data, artifact_path=path_to_data)
        return run.info.run_id


if __name__ == "__main__":
    path_to_data = setup()
    load_raw_data(path_to_data)
    split_raw_data(path_to_data)
    run_id = log_raw_data(path_to_data)
    print(run_id)