# Agentic AI System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![Redis](https://img.shields.io/badge/Redis-6.0+-orange.svg)](https://redis.io/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-yellow.svg)](https://ai.google.dev/)

An intelligent multi-agent AI system powered by Google Gemini, designed for complex task processing through orchestrated agent workflows. The system features a web UI, asynchronous job queuing, and modular agent architecture for scalable AI-driven automation.

## Features

- **Multi-Agent Architecture**: Specialized agents (Retriever, Analyzer, Writer) for sequential task processing
- **Asynchronous Processing**: Redis-based job queue for reliable task management
- **Web Interface**: Intuitive Streamlit UI for task submission and result viewing
- **REST API**: FastAPI backend with OpenAPI documentation
- **LLM Integration**: Powered by Google Gemini 2.5 Flash for advanced reasoning
- **Scalable Design**: Modular components for easy extension and maintenance
- **Real-time Monitoring**: Console logging for agent activities and job status

##  Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit UI  │───▶│   FastAPI API   │───▶│   Redis Queue   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Retriever      │───▶│   Analyzer      │───▶│    Writer       │
│   Agent         │    │   Agent         │    │   Agent         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
       │                       │                       │
       └───────────────────────┼───────────────────────┘
                               ▼
                       Google Gemini API
```

### Components

- **Streamlit App**: User interface for task submission and result display
- **FastAPI Backend**: REST API server handling task dispatch and result retrieval
- **Redis Queue**: Message queue for job management and inter-agent communication
- **Agent Worker**: Asynchronous worker processing jobs through agent pipeline
- **Agents**:
  - **Retriever**: Extracts and gathers relevant information
  - **Analyzer**: Performs in-depth analysis and data processing
  - **Writer**: Generates comprehensive reports and summaries

##  Prerequisites

- Python 3.8+
- Redis server (running on localhost:6379)
- Google Gemini API key

##  Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd agentic_ai_system
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_google_gemini_api_key_here
   ```

5. **Start Redis server**:
   ```bash
   # If using Docker
   docker run -d -p 6379:6379 redis:alpine

   # Or using local Redis installation
   redis-server
   ```

##  Usage

### Development Mode

1. **Start the FastAPI backend**:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start the agent worker** (in a separate terminal):
   ```bash
   python -c "import asyncio; from app.worker import AgentWorker; asyncio.run(AgentWorker().start())"
   ```

3. **Start the Streamlit UI** (in a separate terminal):
   ```bash
   streamlit run streamlit_app.py
   ```

### Production Deployment

Use Docker Compose or container orchestration for production deployment with proper environment management.

## 📖 API Documentation

Once the FastAPI server is running, visit `http://localhost:8000/docs` for interactive API documentation.

### Key Endpoints

- `POST /run-task`: Submit a new task for processing
  ```json
  {
    "task": "Analyze Microsoft business model and write a short report"
  }
  ```

- `GET /result`: Retrieve the latest processing result
  ```json
  {
    "result": "Processed report content..."
  }
  ```

##  Configuration

### Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Redis Configuration

Modify `app/queue.py` to change Redis connection settings:
```python
self.redis = redis.Redis(
    host="127.0.0.1",
    port=6379,
    db=0,
    decode_responses=True
)
```

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- Google Gemini for powerful LLM capabilities
- FastAPI for the robust API framework
- Streamlit for the intuitive web interface
- Redis for reliable queue management

## Support

For questions or issues, please open an issue on GitHub or contact the development team.

---

**Note**: This system requires a valid Google Gemini API key. Ensure you comply with Google's terms of service and API usage policies.