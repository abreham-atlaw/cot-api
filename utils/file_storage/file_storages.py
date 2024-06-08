# Importing necessary libraries and modules
from typing import *
from abc import ABC, abstractmethod
import os

from utils.network.rest_interface import Request, NetworkApiClient


# Abstract base class for FileStorage
class FileStorage(ABC):

    # Abstract method to get the URL of a file
    @abstractmethod
    def get_url(self, path) -> str:
        pass

    # Abstract method to upload a file
    @abstractmethod
    def upload_file(self, file_path: str, upload_path: Union[str, None] = None):
        pass

    # Method to download a file using wget command in the system shell
    def download(self, path, download_path: Union[str, None] = None):
        url = self.get_url(path)
        command = f"wget --no-verbose \"{url}\""
        if download_path is not None:
            command = f"{command} -O {download_path}"
        os.system(command)


class HostingStorage(FileStorage):

    class GetUrlRequest(Request):

        def __init__(self, file_path: str):
            super().__init__(
                "geturl.php",
                get_params={
                    "filename": file_path
                }
            )

        def deserialize_object(self, response) -> object:
            return response

    class UploadFileRequest(Request):

        def __init__(self, filepath: str, upload_path: Optional[str] = None):
            get_params = {}
            if upload_path is not None:
                get_params["path"] = upload_path
            super().__init__(
                "upload.php",
                method=Request.Method.POST,
                get_params=get_params,
                files={
                    "file": filepath
                },
                headers={
                    "Content-Type": None
                }
            )

        def deserialize_object(self, response) -> object:
            return ""

    def __init__(self, host: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__client = NetworkApiClient(host)

    def get_url(self, path) -> str:
        return self.__client.execute(
            self.GetUrlRequest(
                path
            )
        )

    def upload_file(self, file_path: str, upload_path: Union[str, None] = None):
        return self.__client.execute(
            self.UploadFileRequest(
                filepath=file_path,
                upload_path=upload_path
            )
        )
