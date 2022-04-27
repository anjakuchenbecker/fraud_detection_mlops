# TODO: develop training module

# External imports
import mlflow
import argparse
# Internal imports
# NA

def setup():
    """
    Setup the training module
    """

    # Setup the command-line parser
    parser = argparse.ArgumentParser()
    parser.add_argument("mlflow_tracking_uri", 
                        help="Set the MLflow tracking server URI", 
                        type=str)
    args = parser.parse_args()
    
    # Set tracking uri (tracking server and registry server are the same / not separated)
    # No need to set the registry uri in addition, because it defaults to the tracking URI
    mlflow.set_tracking_uri(args.mlflow_tracking_uri)

if __name__ == "__main__":
    setup()
    print("training module: hello world")