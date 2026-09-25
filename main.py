import sys, os

_root = os.path.dirname(os.path.abspath(__file__))
_backend = os.path.join(_root, "backend")

if os.path.exists(_backend):
    os.chdir(_backend)
    if _backend not in sys.path:
        sys.path.insert(0, _backend)

import uvicorn
from app.main import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"[RENDER DEPLOY] Server launching on 0.0.0.0:{port} in {os.getcwd()}")
    uvicorn.run(app, host="0.0.0.0", port=port)