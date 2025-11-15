
# Chatbot FastAPI

### Agentic Chatbot for Blog Generation

## 📝 Overview  
**AI Blog Generator** is a FastAPI-based application that generates blogs, titles, and translated content using **LangGraph** workflow automation and **Groq LLMs**.  
The system supports multilingual blog creation with strict schema validation, deterministic workflow execution, and modular graph-based processing.

---

## 🚀 Features  
- Workflow-driven blog generation using **LangGraph pipelines**  
- Multi-language blog translation  
- Structured output validation with **Pydantic**  
- High-performance inference using **Groq models**  
- Deterministic, node-based LLM processing  
- FastAPI REST API with a modular graph architecture  
- Supports **Python 3.12.0**

---

## 🧰 Tech Stack  
- **Python 3.12.0**  
- **FastAPI**  
- **Uvicorn**  
- **LangGraph**  
- **Groq LLMs**  
  - llama-3.1-8b-instant  
  - qwen/qwen3-32b  
- **Pydantic**  
- Environment-based configuration management

---

### Run the Application

```bash
streamlit run src/app.py
```

The application will open in your default browser at `http://localhost:8501`.

---

## 🏗️ Project Structure

```

CHATBOT_FASTAPI/
│
├── .langgraph_api/               # LangGraph API metadata (automatically generated)
├── .venv/                        # uv-managed virtual environment
├── .vscode/                      # Editor settings
│
├── .gitignore
├── .python-version               # Python version for uv/pyenv
├── .env                          # Environment variables
│
├── app.py                        # Optional entrypoint (FastAPI)
├── main.py                       # Primary FastAPI app entrypoint
├── langgraph.json                # LangGraph workflow configuration
├── pyproject.toml                # uv project file (dependencies + metadata)
│
├── src/
│   ├── __pycache__/
│   │
│   ├── api/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   │
│   │   ├── routes/               # API route handlers
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   └── blog_route.py     # Blog generation/translation endpoint
│   │   │
│   │   └── schema/               # Pydantic models
│   │       ├── __pycache__/
│   │       ├── __init__.py
│   │       ├── blog_schema.py    # Request/response schemas
│   │       └── schema_base.py    # Shared schema base classes
│   │
│   ├── chatbot_fastapi.egg-info/ # Project install metadata
│   │
│   ├── core/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── settings.py           # Settings using Pydantic BaseSettings
│   │   └── use_case_enum.py      # Blog use-case enumeration
│   │
│   ├── graphs/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── blog_graph.py         # Main LangGraph workflow
│   │   └── langsmith.py          # LangSmith tracing/logging
│   │
│   ├── llm/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── groq_llm.py           # Groq LLM client wrapper
│   │
│   ├── nodes/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── blog_node.py          # LangGraph node definitions
│   │
│   ├── states/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── blog_state.py         # Workflow state model
│   │
│   └── utils/
│       ├── __pycache__/
│       └── __init__.py           # Utilities (logger, helpers)
│
└── README.md


```


## 📦 Installation

- Using uv (Package Manager)

```bash
pip install uv or https://docs.astral.sh/uv/guides/install-python/

uv sync
uv run uvicorn main:app --reload

- Add a dependency

uv add fastapi
uv add langgraph
uv add groq

