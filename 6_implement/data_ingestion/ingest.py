# TODO: develop ingestion module

# External imports
import mlflow
import os
import mysql.connector as connection
from sklearn.model_selection import train_test_split
from datetime import datetime
import pandas as pd
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


def load_and_split_raw_data(path_to_data):
    """
    Load raw data (applications) from datasource (mysql db), split into train test and save raw csv-files.
    """

    try:
        # Open connection to database
        db = connection.connect(host="database", 
                                database="db", 
                                user="root", 
                                passwd="",
                                use_pure=True)
        
        # Read all labeled and verified data from application table to pandas dataframe
        query = f"SELECT * FROM applications WHERE is_fraud_verified = 1 AND is_fraud IS NOT NULL;"
        raw_data_applications = pd.read_sql(query,db)
        
        # Close connection
        db.close() #close the connection

        # Define file names
        output_file_all = "raw_data.csv"
        output_file_train = "raw_data_train.csv"
        output_file_test = "raw_data_test.csv"

        # Split raw data
        raw_data_applications_train, raw_data_applications_test = train_test_split(raw_data_applications, test_size=0.30, random_state=42)
        
        # Save to raw_data.csv
        raw_data_applications.to_csv(
            os.path.join(path_to_data, output_file_all), 
            sep=";", 
            encoding="utf-8",
            index=False)
        
        # Save to raw_data_train.csv
        raw_data_applications_train.to_csv(
            os.path.join(path_to_data, output_file_train), 
            sep=";", 
            encoding="utf-8",
            index=False)
        
        # Save to raw_data_test.csv
        raw_data_applications_test.to_csv(
            os.path.join(path_to_data, output_file_test), 
            sep=";", 
            encoding="utf-8",
            index=False)

        # Start a new MLflow run, as we are in the first step in our pipeline
        current_date = datetime.now().strftime("%Y-%m-%d")
        run_name = f"applications incl. ground truth until {current_date}"
        with mlflow.start_run(run_name=run_name) as run:
            # Log raw data files
            mlflow.log_artifact(os.path.join(path_to_data, output_file_all), artifact_path=path_to_data)
            mlflow.log_artifact(os.path.join(path_to_data, output_file_train), artifact_path=path_to_data)
            mlflow.log_artifact(os.path.join(path_to_data, output_file_test), artifact_path=path_to_data)
        return run.info.run_id

    except Exception as e:
        db.close()

if __name__ == "__main__":
    path_to_data = setup()
    run_id = load_and_split_raw_data(path_to_data)
    print(run_id)