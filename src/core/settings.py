from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()

class Settings(BaseSettings):

    GROQ_API_KEY:str = os.getenv("GROQ_API_KEY")
    # GROQ_MODEL_NAME:str = "qwen/qwen3-32b"
    # GROQ_MODEL_NAME:str = "llama-3.1-8b-instant"
    GROQ_MODEL_NAME:str = "qwen/qwen3-32b"
    LANGCHAIN_PROJECT:str="Fastapi_blog_generator"
    LANGCHAIN_API_KEY:str=os.getenv("LANGCHAIN_API_KEY")

    API_TAG_V1:str = "/api/v1"
     



settings = Settings()