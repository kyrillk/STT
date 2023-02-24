


ARTIFACT_DIR: str = "artifacts"
PIPELINE_NAME: str = "stt"

MAX_TARGET_LENGTH: int = 200

# s3 buckets
DATA_BUCKET_URI: str ="s3://speech-to-text-project/data/"

# common file names
METADATA_DIR: str = "metadata"
METADATA_FILE_NAME: str = "metadata.csv"
WAVS_FILE_PATH: str = "wavs.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

# Data Ingestion related constant
DATA_DIR_NAME: str = "data"
DOWNLOAD_DIR: str = 'download_data'
ZIP_FILE_NAME: str = "LJSpeech-1.1.zip"
UNZIPPED_FOLDER_NAME: str = "LJSpeech-1.1"

# Data Preprocessing related constants
DATA_PREPROCESSING_ARTIFACTS_DIR: str = "data_preprocessing_artifacts"
DATA_PREPROCESSING_TRAIN_DIR: str = "train"
DATA_PREPROCESSING_TEST_DIR: str = "test"
TRAIN_TEST_SPLIT_RATIO:int = 0.99