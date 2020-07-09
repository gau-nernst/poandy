import json

from poandy.util.objectless import Objectless

class Utils(Objectless):
    _config = None

    @classmethod
    def _load_config(cls):
        with open("config.json") as f:
            cls._config = json.load(f)
        with open(cls._config["secrets_path"]) as f:
            secrets = json.load(f)
        cls._config.update(secrets)

    @classmethod
    def get_config(cls):
        if not cls._config:
            cls._load_config()
        return cls._config

    @classmethod
    def get_authorization(cls):
        token = cls.get_config()["token"]
        return {"Authorization": f"Bearer {token}"}