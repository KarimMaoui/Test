import yaml
from pathlib import Path

CONFIG_PATH = Path("config.yml")

DEFAULT_CONFIG = {
    "sec_user_agent": "YourName Contact your.email@example.com",
    "output_dir": "out",
    "digest_dir": "digest"
}

def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as f:
            return yaml.safe_load(f)
    return DEFAULT_CONFIG

def save_default_config():
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(DEFAULT_CONFIG, f)
    print(f"Default config saved to {CONFIG_PATH}")
