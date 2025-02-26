class DockerVolumeSync:
    def __init__(self):
        pass

    def sync_folder_to_volume(self, folder: str, volume: str):
        try:
            os.system(f"cp -r {folder} {volume}")
        except Exception as e:
            raise STTException(e, sys)