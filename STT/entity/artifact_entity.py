from dataclasses import dataclass

# Data ingestion artifacts
@dataclass
class DataIngestionArtifacts:
    downloaded_data_path: str
    extracted_data_path: str

@dataclass
class DataPreprocessingArtifacts:
    train_data_path: str
    test_data_path: str