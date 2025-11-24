import os
import pandas
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at {file_path}")
        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("SUccessfully read YAML file")
            return config
    except Exception as e:
        logger.log("Error while reading YAML file")
        raise CustomException("Failed to raise custom exception", e)