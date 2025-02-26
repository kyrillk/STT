import os
import sys

from STT.exceptions import STTException
from STT.logger import logging

from STT.cloud_storage.s3_operations import S3Sync
from STT.entity.config_entity import ModelPusherConfig
from STT.entity.artifact_entity import ModelEvaluationArtifacts, ModelPusherArtifacts

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig,model_evaluation_artifacts: ModelEvaluationArtifacts):
        try:
            self.model_pusher_config = model_pusher_config
            self.model_evaluation_artifacts = model_evaluation_artifacts
        except Exception as e:
            raise STTException(e, sys)

    def initiate_model_pusher(self):
        try:
            logging.info("Initiating model pusher component")
            if self.model_evaluation_artifacts.is_model_accepted:
                trained_model_path = self.model_evaluation_artifacts.trained_model_path


                volume_model_folder_path = self.model_pusher_config.s3_model_path

                # chagne to volume?
                volume_sync = DockerVolumeSync()
                volume_sync.sync_folder_to_volume(folder=trained_model_path, __path__ = volume_model_folder_path)
                message = "Model Pusher pushed the current Trained model to Production server storage"
                response = {"is model pushed": True, "S3_model": volume_model_folder_path,"message" : message}
                logging.info(response)
            else:
                volume_model_folder_path = self.model_pusher_config.volume_model_path
                message = "Current Trained Model is not accepted as model in Production has better accuracy"
                response = {"is model pushed": False, "S3_model":volume_model_folder_path,"message" : message}
                logging.info(response)
            
            model_pusher_artifacts = ModelPusherArtifacts(response=response)
            return model_pusher_artifacts

        except Exception as e:
            raise STTException(e, sys)