# TODO: develop data validation module

# External imports
import mlflow
import os
import argparse
import great_expectations as ge
# Internal imports
# NA


# TBD
MLFLOW_TRACKING_SERVER_URL = os.environ.get("MLFLOW_TRACKING_SERVER_URL")
MLFLOW_EXPERIMENT_NAME = os.environ.get("MLFLOW_EXPERIMENT_NAME")
MLFLOW_RUN_ID = ""
PATH_TO_DATA = "output/data"
PATH_TO_REPORTS = "output/reports"
OUTPUT_FILE = "raw_data_summary_statistics.csv"
RAW_DATA_FILES = [f"{PATH_TO_DATA}/raw_data.csv", 
                        f"{PATH_TO_DATA}/raw_data_train.csv", 
                        f"{PATH_TO_DATA}/raw_data_test.csv"]

def setup():
    """
    Setup the validation module
    """

    # Setup the command-line parser
    parser = argparse.ArgumentParser()
    parser.add_argument("mlflow_run_id",
                        help="Set the MLflow run id",
                        type=str)
    args = parser.parse_args()
    global MLFLOW_RUN_ID
    MLFLOW_RUN_ID = str(args.mlflow_run_id)

    # Set tracking uri (tracking server and registry server are the same / not separated)
    # No need to set the registry uri in addition, because it defaults to the tracking URI
    mlflow.set_tracking_uri(MLFLOW_TRACKING_SERVER_URL)
     # Set experiment
    mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)

    # Create output directory for reports
    os.makedirs(PATH_TO_REPORTS, exist_ok=True)

    # Check whether raw data files exist
    for file in RAW_DATA_FILES:
        if not os.path.exists(file):
            raise FileNotFoundError(f"raw data file not found {file}")

def check_schema_for_new_data(raw_data_files):
    """
    Check schema of new data to detect errors in upstream system (data source).
    """
    
    # Dict for MLflow parameter logging
    mlflow_run_parameters = {}

    # Check schema for new data
    for file in raw_data_files:
        # Read raw data file
        raw_data_applications = ge.read_csv(file,
                            sep=";",
                            encoding="utf-8")
        
        # Check 1: specific columns must exist in all raw data files
        result = raw_data_applications.expect_table_columns_to_match_set(
            column_set=["address", "application_request_time", "application_type",
                        "birthday", "browser", "city", "device_type", "email",
                        "first_name", "is_fraud", "is_fraud_verified", "last_name",
                        "marital_status", "phone", "title", "trx"
            ], 
            exact_match=False
        )

        if not result.success:
            raise AssertionError(result)

        # Check 2: is_fraud column value must not be null
        result = raw_data_applications.expect_column_values_to_not_be_null(
            column="is_fraud"
        )

        if not result.success:
            raise AssertionError(result)
        
        # Check 3: is_fraud column value must be 0 or 1
        result = raw_data_applications.expect_column_distinct_values_to_be_in_set(
            column="is_fraud",
            value_set=[0,1]
        )

        if not result.success:
            raise AssertionError(result)
        
        # Populate parameter information to dict
        param_name = False
        if file.endswith("raw_data.csv"):
            param_name = "num_instances_all"
            compute_summary_statistics_for_new_data(raw_data_applications)
        if file.endswith("raw_data_train.csv"):
            param_name = "num_instances_train"
        if file.endswith("raw_data_test.csv"):
            param_name = "num_instances_test"
        mlflow_run_parameters[param_name] = raw_data_applications.shape[0]
        
        # Attach further information to already created MLflow run
        with mlflow.start_run(run_id=MLFLOW_RUN_ID) as run:
            # Log batch of parameters
            mlflow.log_params(mlflow_run_parameters)

def compute_summary_statistics_for_new_data(df):
    """
    Compute summary statistics (descriptive) for new data for later data drift detection
    """

    # Create csv file based on pd.df.describe including all data types
    df.describe(include="all").T.to_csv(os.path.join(PATH_TO_REPORTS, OUTPUT_FILE), 
                                        encoding="utf-8")
    
    # Attach further information to already created MLflow run
    with mlflow.start_run(run_id=MLFLOW_RUN_ID) as run:
        # Log summary statistics csv
        mlflow.log_artifact(os.path.join(PATH_TO_REPORTS, OUTPUT_FILE), artifact_path=PATH_TO_REPORTS)

if __name__ == "__main__":
    setup()
    check_schema_for_new_data(RAW_DATA_FILES)
    print("data validation succeeded:", RAW_DATA_FILES)