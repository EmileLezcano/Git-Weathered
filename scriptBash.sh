#!/bin/bash
set -e  # Salir si algún comando falla

mv .venv.sample .venv

echo "Requisitos de instalación..."
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
