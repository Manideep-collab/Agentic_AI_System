import redis
import json

class RedisQueue:
    def __init__(self):
        self.redis = redis.Redis(
            host="127.0.0.1",
            port=6379,
            db=0,
            decode_responses=True
        )
        self.agent_queue = "agent_jobs"
        self.result_key = "final_result"

    def enqueue_agent_job(self, job: dict):
        self.redis.lpush(self.agent_queue, json.dumps(job))

    def dequeue_agent_job(self):
        job = self.redis.rpop(self.agent_queue)
        return json.loads(job) if job else None

    def save_result(self, result: str):
        self.redis.set(self.result_key, result)
        print(f"✅ Result saved to Redis: {self.result_key}")

    def get_result(self):
        result = self.redis.get(self.result_key)
        print(f"📥 Retrieved result from Redis: {result}")
        return result
