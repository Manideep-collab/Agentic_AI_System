from app.queue import RedisQueue

class Orchestrator:
    def __init__(self):
        self.queue = RedisQueue()

    def dispatch(self, task: str):
        # First agent only
        self.queue.enqueue_agent_job({
            "agent": "retriever",
            "input": task
        })
