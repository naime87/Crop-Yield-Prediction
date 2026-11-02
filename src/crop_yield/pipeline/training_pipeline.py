import sys
from src.crop_yield.exception import CropYieldException
from src.crop_yield.logger import logging
from src.crop_yield.components.data_ingestion import DataIngestion

from src.crop_yield.entity.config_entity import (
    DataIngestionConfig,
)

from src.crop_yield.entity.artifact_entity import (
    DataIngestionArtifact,
)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()


    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Entered the start_data_ingestion_method of TrainPipeline")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Excited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise CropYieldException(e, sys) from e

    def run_pipeline(self,) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
        except Exception as e:
            raise CropYieldException(e, sys)