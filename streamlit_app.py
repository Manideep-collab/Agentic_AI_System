import streamlit as st
import requests
import time

BACKEND_RUN = "http://127.0.0.1:8000/run-task"
BACKEND_RESULT = "http://127.0.0.1:8000/result"

st.set_page_config(page_title="Agentic AI System", layout="centered")
st.title("🤖 Agentic AI System (Gemini-powered)")

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

        # Poll for result (max 30 seconds)
        with st.spinner("Agents are working..."):
            result = None
            for _ in range(15):  # 15 × 2s = 30s
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
