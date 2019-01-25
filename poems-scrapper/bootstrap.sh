if [ ! -d ".env" ]; then
    python -m venv .env
fi

source .env/Scripts/activate && pip install -r requirements.txt