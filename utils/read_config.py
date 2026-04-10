import os

import yaml

from utils.path_utils import CONFIG_DIR


class ConfigReader:
    def __init__(self, env="qa"):
        self.env = env
        self.config_data = self._load_config()

    def _load_config(self):
        config_path = CONFIG_DIR / f"{self.env}.yaml"
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file) or {}

    def get(self, key, default=None):
        env_map = {
            "base_url": "BASE_URL",
            "username": "APP_USERNAME",
            "password": "APP_PASSWORD",
        }
        env_key = env_map.get(key)
        if env_key and os.getenv(env_key):
            return os.getenv(env_key)
        return self.config_data.get(key, default)
