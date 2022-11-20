import os

from server import create_app

ENVIRONMENT = "development" if os.environ.get("PORT") is None else "production"
DEBUG = ENVIRONMENT == "development"

app = create_app(debug_mode=DEBUG)
