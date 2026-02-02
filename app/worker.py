import asyncio
from unittest import result
from app.queue import RedisQueue
from app.agents import RetrieverAgent, AnalyzerAgent, WriterAgent

class AgentWorker:
    def __init__(self):
        self.queue = RedisQueue()
        self.retriever = RetrieverAgent()
        self.analyzer = AnalyzerAgent()
        self.writer = WriterAgent()

    async def start(self):
        print("🟢 Agent worker started")

        while True:
            job = self.queue.dequeue_agent_job()

            if not job:
                await asyncio.sleep(0.5)
                continue

            agent = job["agent"]
            input_data = job["input"]

            # 🔹 RETRIEVER
            if agent == "retriever":
                result = await self.retriever.run(input_data)
                print("[RETRIEVER RESULT]\n", result)

                # Enqueue next step
                self.queue.enqueue_agent_job({
                    "agent": "analyzer",
                    "input": result
                })

            # 🔹 ANALYZER
            elif agent == "analyzer":
                result = await self.analyzer.run(input_data)
                print("[ANALYZER RESULT]\n", result)

                # Enqueue next step
                self.queue.enqueue_agent_job({
                    "agent": "writer",
                    "input": result
                })

            elif agent == "writer":
                result = await self.writer.run(input_data)
                print("[WRITER RESULT]\n", result)

                # Save final result for UI
                self.queue.save_result(result)

