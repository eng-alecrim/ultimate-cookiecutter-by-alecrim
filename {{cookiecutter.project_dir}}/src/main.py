from common.logging import configure_logging
from loguru import logger
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
project_name = os.getenv("PROJECT_NAME", "{{cookiecutter.project_dir}}")

configure_logging(project_name=project_name, log_to_file=True)


def main() -> None:
    logger.debug("Hello from {{cookiecutter.project_dir}}!")
    return None


if __name__ == "__main__":
    main()
