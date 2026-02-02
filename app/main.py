from fastapi import FastAPI
from app.orchestrator import Orchestrator
from app.queue import RedisQueue

app = FastAPI()
orchestrator = Orchestrator()
queue = RedisQueue()

@app.post("/run-task")
async def run_task(request: dict):
    task = request.get("task")
    orchestrator.dispatch(task)

    return {
        "message": "Task accepted and dispatched",
        "task": task
    }

# ✅ NEW
@app.get("/result")
async def get_result():
    result = queue.get_result()
    return {
        "result": result
    }
