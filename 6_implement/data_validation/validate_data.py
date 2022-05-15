# TODO: develop data validation module

# External imports
import mlflow
import os
import great_expectations as ge
# Internal imports
# NA


def setup():
    """
    Setup the validation module
    """

    # Retrieve environment variables
    MLFLOW_TRACKING_SERVER_URL = os.environ.get("MLFLOW_TRACKING_SERVER_URL")
    MLFLOW_EXPERIMENT_NAME = os.environ.get("MLFLOW_EXPERIMENT_NAME")

    # Set tracking uri (tracking server and registry server are the same / not separated)
    # No need to set the registry uri in addition, because it defaults to the tracking URI
    mlflow.set_tracking_uri(MLFLOW_TRACKING_SERVER_URL)
     # Set experiment
    mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)

    # Check whether raw data files exist
    path_to_data = "output/data"
    raw_data_files = [f"{path_to_data}/raw_data.csv", 
                        f"{path_to_data}/raw_data_train.csv", 
                        f"{path_to_data}/raw_data_test.csv"]

    for file in raw_data_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"raw data file not found {file}")
    
    return raw_data_files

def check_schema_for_new_data(raw_data_files):
    """
    Check schema of new data to detect errors in upstream system (data source)
    """
    # TODO
    # column count, column names, number of unique levels (categorical)
    pass

def compute_summary_statistics_for_new_data():
    """
    TBD
    """
    # TODO
    pass

if __name__ == "__main__":
    raw_data_files = setup()
    print(raw_data_files)