from pathlib import Path
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


# Set up git repository
def init_git():
    try:
        subprocess.check_call(
            ["git", "init", "-b", "{{ cookiecutter.default_branch }}"],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        subprocess.check_call(
            ["git", "config", "--global", "--add", "safe.directory", PROJECT_DIRECTORY],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        subprocess.check_call(
            ["git", "add", "."],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        subprocess.check_call(
            ["git", "commit", "-m", "Initial commit from cookicutter."],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        print("Git repository initialized successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing git repository: {e}")


def copy_env():
    try:
        subprocess.check_call(
            ["mv", "src/config/.env.example", "src/config/.env"],
            cwd=PROJECT_DIRECTORY,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(".env file created sucessfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating .env file: {e}")


def create_gitingore():
    try:
        subprocess.check_call(
            "echo '#Exclude everything except the gitignore\n*\n!.gitignore' > data/.gitignore",
            cwd=PROJECT_DIRECTORY,
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error creating .gitignore file in data folder: {e}")




def remove_directory(dir_path: Path):
    for item in dir_path.glob("*"):
        if item.is_dir():
            remove_directory(item)
            item.rmdir()
        else:
            item.unlink(missing_ok=True)
    dir_path.rmdir()

# Values from cookiecutter context
include_bsg = "{{ cookiecutter.include_bronze_silver_gold }}"  # rendered value
include_ml = "{{ cookiecutter.include_ml }}"
include_vis = "{{ cookiecutter.include_visualization }}"
include_documentation = "{{ cookiecutter.include_documentation }}"

paths_to_remove = []

if include_bsg != "yes":
    paths_to_remove += [
        "data/bronze",
        "data/silver",
        "data/gold",
        "packages/core/src/core/data/bronze.py",
        "packages/core/src/core/data/silver.py",
        "packages/core/src/core/data/gold.py",
    ]
if include_bsg == "yes":
    paths_to_remove += ["packages/core/src/core/data/processing.py"]

if include_ml != "yes":
    paths_to_remove += ["packages/core/src/core/models"]

if include_vis != "yes":
    paths_to_remove += ["packages/core/src/core/visualization"]

if include_documentation != "yes":
    paths_to_remove += ["mkdocs.yml"]

# Now remove
for path_str in paths_to_remove:
    path = Path(path_str)
    if not path.exists():
        continue
    if path.is_file():
        path.unlink(missing_ok=True)
    elif path.is_dir():
        remove_directory(path)

create_gitingore()
if "{{ cookiecutter.use_git }}" == "Yes":
    init_git()

