from src.crop_yield.logger import logging
from src.crop_yield.exception import CropYieldException
import sys
import dotenv

from dotenv import load_dotenv

load_dotenv()

logging.info("Welcome to our custom log")

from src.crop_yield.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()

