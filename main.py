import sys, os

_root = os.path.dirname(os.path.abspath(__file__))
_backend = os.path.join(_root, "backend")

if _backend in sys.path:
    sys.path.remove(_backend)
sys.path.insert(0, _backend)

import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"[LIVE SERVER] Starting FastAPI on 0.0.0.0:{port} with sys.path[0]={_backend}")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)