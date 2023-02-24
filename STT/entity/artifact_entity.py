from dataclasses import dataclass

# Data ingestion artifacts
@dataclass
class DataIngestionArtifacts:
    downloaded_data_path: str
    extracted_data_path: str