# Dockerfile for automated continuous training (CT) pipeline
# Including: miniconda, git, mlflow, great-expectations
# https://hub.docker.com/r/continuumio/miniconda3
FROM continuumio/miniconda3:4.11.0

# Ensure experimental-operational symmetry
# Pipeline implementation that is used in the development or experiment environment is used in the preproduction and production environment
COPY 6_implement/docker/dev_environment/requirements/requirements.txt opt/custom/requirements.txt
COPY 6_implement/data_ingestion/ opt/custom/
COPY 6_implement/data_validation/ opt/custom/
COPY 6_implement/data_preprocessing/ opt/custom/
COPY 6_implement/model_training/ opt/custom/
COPY 6_implement/model_evaluation/ opt/custom/
COPY 6_implement/model_validation/ opt/custom/
COPY 6_implement/model_deployment/ opt/custom/

RUN apt-get -y update \
    && apt-get -y install git
RUN pip install -U pip && \
    pip install -r opt/custom/requirements/requirements.txt