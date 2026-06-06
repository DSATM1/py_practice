#!/usr/bin/env bash
set -euo pipefail

# Run from repo root. Creates a venv (if not present) and installs requirements.
PYENV_DIR=".venv"
python3 -m venv ${PYENV_DIR}
source ${PYENV_DIR}/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r ai_week1/requirements.txt

echo "Setup complete. To start Jupyter Lab: source ${PYENV_DIR}/bin/activate && jupyter lab"
