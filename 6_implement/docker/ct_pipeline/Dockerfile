# Dockerfile for CT pipeline
# https://hub.docker.com/r/continuumio/miniconda3
FROM continuumio/miniconda3

COPY 6_implement/data_ingestion/ opt/custom/fraud_detection_ct_pipeline/
COPY 6_implement/data_validation/ opt/custom/fraud_detection_ct_pipeline/
COPY 6_implement/data_preprocessing/ opt/custom/fraud_detection_ct_pipeline/
COPY 6_implement/model_training/ opt/custom/fraud_detection_ct_pipeline/
COPY 6_implement/model_evaluation/ opt/custom/fraud_detection_ct_pipeline/
COPY 6_implement/model_validation/ opt/custom/fraud_detection_ct_pipeline/
COPY 6_implement/model_deployment/ opt/custom/fraud_detection_ct_pipeline/