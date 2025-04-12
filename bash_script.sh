#!/bin/bash

# Create main directories
mkdir -p .github/workflows
mkdir -p config
mkdir -p data/{bronze,silver,gold}
mkdir -p docs/{imgs,api}
mkdir -p log
mkdir -p notebooks
mkdir -p packages/common/src/common
mkdir -p packages/core/src/core/{data,models,visualization}
mkdir -p tests/{unit,integration}

# Create empty files (.gitkeep) to ensure git tracks empty directories
touch data/bronze/.gitkeep data/silver/.gitkeep data/gold/.gitkeep
touch docs/imgs/.gitkeep docs/api/.gitkeep
touch log/.gitkeep

# Create __init__.py files
touch config/__init__.py
touch packages/common/src/common/__init__.py
touch packages/core/src/core/__init__.py
touch packages/core/src/core/data/__init__.py
touch packages/core/src/core/models/__init__.py
touch packages/core/src/core/visualization/__init__.py
touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/integration/__init__.py

# Create important Python module files
touch config/settings.py
touch packages/common/src/common/config.py
touch packages/common/src/common/logging.py
touch packages/common/src/common/utils.py
touch packages/core/src/core/data/bronze.py
touch packages/core/src/core/data/silver.py
touch packages/core/src/core/data/gold.py
touch packages/core/src/core/models/train.py
touch packages/core/src/core/models/evaluate.py
touch packages/core/src/core/visualization/plots.py
touch tests/unit/test_common.py
touch tests/unit/test_core.py
touch tests/integration/test_pipeline.py

# Create configuration files
touch .github/workflows/ci.yml
touch .gitignore
touch .pre-commit-config.yaml
touch LICENSE
touch README.md
touch pyproject.toml
touch mkdocs.yml
touch packages/common/pyproject.toml
touch packages/core/pyproject.toml

# Create sample notebook (just the empty file for now)
touch notebooks/01_exploratory_data_analysis.ipynb

# Create docs homepage
touch docs/index.md

echo "Project structure created successfully!"
