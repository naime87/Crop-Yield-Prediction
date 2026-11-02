import os
from datetime import date


DATABASE_NAME = "Crop_Yield"

COLLECTION_NAME = "crop_yield"

MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME: str = "crop_yield"
ARTIFACT_DIR: str = "artifact"

TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = "test.csv"

FILE_NAME: str = "crop_yield"
MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = ""
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

"""
Data Ingestion related Constants
"""
DATA_INGESTION_COLLECTTION_NAME: str = "crop_yield"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2