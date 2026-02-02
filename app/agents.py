import asyncio
from app.llm import call_gemini

class RetrieverAgent:
    async def run(self, task: str):
        prompt = f"""
You are a research agent.

Task:
{task}

Extract key factual points and background information.
Use concise bullet points.
"""
        return call_gemini(prompt)


class AnalyzerAgent:
    async def run(self, retrieved_data: str):
        prompt = f"""
You are a business analyst.

Analyze the information below and identify:
- Business model components
- Revenue streams
- Strategic advantages

Information:
{retrieved_data}
"""
        return call_gemini(prompt)


class WriterAgent:
    async def run(self, analysis: str):
        prompt = f"""
You are a professional business writer.

Using the analysis below, write a clear and structured report
(3–5 short paragraphs).

Analysis:
{analysis}
"""
        return call_gemini(prompt)
