# main.py

import app.assets

from uvicorn import run

from app.app import app


if __name__ == "__main__":
      run(
            app=app,
            host="0.0.0.0",
            port=8080,
            log_level="debug",
      )
else:
      pass