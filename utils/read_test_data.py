import json
from utils.path_utils import TEST_DATA_DIR


class TestDataReader:
    @staticmethod
    def get_json_data(file_name):
        file_path = TEST_DATA_DIR / file_name

        if not file_path.exists():
            raise FileNotFoundError(f"Test data file not found at: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)