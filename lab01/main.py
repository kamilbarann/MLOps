import os
import yaml
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_file = f"config/.env.{environment}"
    load_dotenv(env_file)


def export_secrets() -> None:
    with open("secrets.yaml", "r") as secrets_file:
        secrets = yaml.safe_load(secrets_file)

    for variable_name, variable_value in secrets.items():
        os.environ[variable_name] = str(variable_value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
