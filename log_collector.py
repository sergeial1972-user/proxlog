#imports
from pathlib import Path
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from typing import List

#dotenv
load_dotenv()

#log dir
log_dir = Path("/var/log")

#logfiles paths
def read_log_paths() -> List[Path]:
    paths = [p for p in log_dir.rglob('*.log') if p.is_file()]
    return paths

# fastapi app
app = FastAPI(title="log_collector")

@app.get("/paths")
async def get_log_paths():
    log_paths = read_log_paths()
    return {
        "paths": [str(p) for p in log_paths],
        "count": len(log_paths)
    }

@app.get("/log/{log_path:path}")
async def read_log(log_path: str):
    log_file = Path(log_path)
    if not log_file.exists() or not log_file.is_file():
        raise HTTPException(404, "NotFound")
    content = log_file.read_text(encoding='utf-8', errors='ignore')
    return {
        "path": log_path,
        "size": len(content),
        "content": content[-10000:]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=os.getenv('HOST', '0.0.0.0'), port=int(os.getenv('PORT', 8081)), reload=True)
