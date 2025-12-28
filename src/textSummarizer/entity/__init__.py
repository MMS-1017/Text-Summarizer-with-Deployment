from dataclasses import dataclass
from pathlib import Path

# This code defines an immutable configuration object for the Data Ingestion stage of your pipeline.
# Instead of passing many parameters separately, everything is grouped into one strongly-typed object.
@dataclass(frozen=True) # to avoid writing the constructor manually, frozen to make it immutable
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir 
        )

        return data_ingestion_config