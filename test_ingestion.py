from networksecurity.components import data_ingestion
from networksecurity.logging.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
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
    except Exception as e: 
       raise NetworkSecurityException(error_message="Error occurred during data ingestion", error_details=str(e))
 
