import streamlit as st
import requests
import time

BACKEND_RUN = "http://127.0.0.1:8000/run-task"
BACKEND_RESULT = "http://127.0.0.1:8000/result"

st.set_page_config(page_title="Agentic AI System", layout="centered")
st.title("🤖 Agentic AI System (Gemini-powered)")

st.info("⚠️ Ensure the agent worker is running in a separate terminal: `python -c \"import asyncio; from app.worker import AgentWorker; asyncio.run(AgentWorker().start())\"`")

task = st.text_area(
    "Enter a complex task",
    placeholder="Analyze Microsoft business model and write a short report"
)

if st.button("Run Task"):
    if not task.strip():
        st.warning("Please enter a task.")
    else:
        # Dispatch task
        requests.post(BACKEND_RUN, json={"task": task}, timeout=10)
        st.success("Task dispatched! Waiting for agents to finish...")

        # Poll for result (max 60 seconds)
        with st.spinner("Agents are working..."):
            result = None
            for _ in range(30):  # 30 × 2s = 60s
                time.sleep(2)
                response = requests.get(BACKEND_RESULT, timeout=5)
                result = response.json().get("result")
                if result:
                    break

        if result:
            st.subheader("📄 Final Report")
            st.write(result)
        else:
            st.error("Timed out waiting for result. Check worker console.")
