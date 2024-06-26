
from SummarEase.constants import *
from SummarEase.utils.common import read_yaml, create_directories
from SummarEase.entity import (DataIngestionConfig,
                               DataValidationConfig,
                               DataTransformationConfig)
from pathlib import Path

class ConfigurationManager:
    def __init__(self, config_filepath=None, params_filepath=None):
        self.config_filepath = Path(config_filepath or CONFIG_FILE_PATH)
        self.params_filepath = Path(params_filepath or PARAMS_FILE_PATH)
        
        self.config = read_yaml(self.config_filepath)
        self.params = read_yaml(self.params_filepath)
        
        create_directories([self.config.artifacts_root])
           
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config    
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config
    