from networksecurity.components import data_ingestion,data_validation
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.logging.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig,DataTransformationConfig, ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == '__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config)
        data_ingestion = data_ingestion.DataIngestion(dataingestionconfig)
        logging.info('Initiating data ingestion')
        dataingestionartifct = data_ingestion.initiate_data_ingestion()
        print(dataingestionconfig)
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(dataingestionartifct,data_validation_config)
        logging.info("Initiate Data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info('data Validation Completed')
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        logging.info("Data transformation started")
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_config)
        logging.info(data_transformation_artifact)
        logging.info("model training started")
        model_trainer_config = ModelTrainerConfig(training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("model training artifact created")
        
        

    except Exception as e: 
       raise NetworkSecurityException(error_message="Error occurred during data ingestion", error_details=str(e))
 
