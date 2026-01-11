import yaml
from networksecurity.logging.logger import logging
from networksecurity.logging.exception import NetworkSecurityException
import os,sys
import numpy as np
import pickle

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) 
