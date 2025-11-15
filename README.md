
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
├── .langgraph_api/              # LangGraph API metadata (optional)
├── .venv/                       # Virtual environment
├── .vscode/                     # VSCode settings
├── .gitignore
├── .python-version
├── .env                         # Environment variables
├── app.py                       # Alternate entrypoint (optional)
├── main.py                      # Main FastAPI application entrypoint
├── langgraph.json               # LangGraph configuration
├── pyproject.toml               # Project metadata + dependencies
│
├── src/
│   ├── __pycache__/
│   │
│   ├── api/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   │
│   │   ├── routes/              # API route handlers
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   └── blog_route.py    # /blog or /generate endpoint
│   │   │
│   │   └── schema/              # Pydantic schemas
│   │       ├── __pycache__/
│   │       ├── __init__.py
│   │       ├── blog_schema.py   # Request/response schemas
│   │       └── schema_base.py   # Base schemas/validators
│   │
│   ├── chatbot_fastapi.egg-info/  # Python package metadata
│   │
│   ├── core/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── settings.py          # Config + environment settings
│   │   └── use_case_enum.py     # Enum for blog use cases
│   │
│   ├── graphs/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── blog_graph.py        # Blog workflow graph
│   │   └── langsmith.py         # LangSmith instrumentation
│   │
│   ├── llm/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── groq_llm.py          # Groq API wrapper client
│   │
│   ├── nodes/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── blog_node.py         # LangGraph nodes for title/content/translation
│   │
│   ├── states/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── blog_state.py        # Workflow state object
│   │
│   └── utils/
│       ├── __pycache__/
│       └── __init__.py          # Utilities module
│
└── README.md (your file)


```


## 📦 Installation

```bash
git clone <repository-url>
cd <project-directory>

python -m venv .venv
.venv\Scripts\activate   # On Windows
# OR
source .venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt
