# TODO: develop evaluation module

# External imports
import mlflow
import argparse
# Internal imports
# NA


def setup():
    """
    Setup the evaluation module
    """

    # Setup the command-line parser
    parser = argparse.ArgumentParser()
    parser.add_argument("mlflow_tracking_uri",
                        help="Set the MLflow tracking server URI",
                        type=str)
    parser.add_argument("mlflow_run_id",
                        help="Set the MLflow run id",
                        type=str)
    args = parser.parse_args()

    # Set tracking uri (tracking server and registry server are the same / not separated)
    # No need to set the registry uri in addition, because it defaults to the tracking URI
    mlflow.set_tracking_uri(args.mlflow_tracking_uri)
    # Get details from given run
    run = mlflow.get_run(args.mlflow_run_id)
    return run


def load_metric_expections():
    """
    TODO
    """

    # TODO
    pass


def evaluate_model():
    """
    TODO
    """

    pass


if __name__ == "__main__":
    run = setup()
    print(run.data.params)