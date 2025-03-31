import os
import pandas
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml
import pandas as pd
import numpy as np

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if  not os.path.exists(file_path):
            raise FileNotFoundError(f"files is not given path")
        with open(file_path, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("successfully read the YAML file")
            return config
    except Exception as e:
        logger.error("Failed to read", e)
        raise CustomException("Error while reading YAML file", e)
    

def load_data(path):
    try:
        logger.info("Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error loading the data {e}")
        raise CustomException("Failed to load data" , e)