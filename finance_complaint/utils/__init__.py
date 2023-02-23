import os
import sys
import shutil
import yaml
from typing import List
from pyspark.sql import DataFrame
from finance_complaint.exception import FinanceException
from finance_complaint.logger import logger


def write_yaml_file(file_path: str, data: dict = None):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as yaml_file:
            if data is not None:
                yaml.dump(data, yaml_file)
    except Exception as e:
        raise FinanceException(e, sys)


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise FinanceException(e, sys) from e



def create_directories(directories_list: List[str], new_directory=False):
    try:

        for dir_path in directories_list:
            if dir_path.startswith("s3"):
                continue
            if os.path.exists(dir_path) and new_directory:
                shutil.rmtree(dir_path)
                logger.info(f"Directory removed: {dir_path}")
            os.makedirs(dir_path, exist_ok=True)
            logger.info(f"Directory created: {dir_path}")
    except Exception as e:
        raise FinanceException(e, sys)
