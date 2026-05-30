class WorkspaceSession:

    def __init__(self):
        self._target_directory: str = ""

    def set_directory(self, path: str) -> None:
        self._target_directory = path

    def get_directory(self) -> str:
        return self._target_directory

    def is_connected(self) -> bool:
        return bool(self._target_directory)
