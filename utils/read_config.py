from pathlib import Path
import yaml


class ConfigReader:
    def __init__(self, env="qa"):
        self.env = env
        self.config_data = self._load_config()

    def _load_config(self):
        project_root = Path(__file__).resolve().parent.parent
        config_path = project_root / "config" / f"{self.env}.yaml"

        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found at: {config_path}")

        with open(config_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def get(self, key, default=None):
        return self.config_data.get(key, default)