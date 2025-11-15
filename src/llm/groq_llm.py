from langchain_groq import ChatGroq
from src.core import settings



class GroqLLM:
    """Create group model
    """
    def __init__(self, model:str="", api_key: str=""):
        """_summary_

        Args:
            model (str, optional): _description_. Defaults to settings.model"".
            api_key (str, optional): _description_. Defaults to settings api key"".
        """
        self.api_key = model if model  else settings.GROQ_API_KEY 
        self.model = api_key if api_key else settings.GROQ_MODEL_NAME
        
    def get_model(self):
        try:
            llm = ChatGroq(api_key=self.api_key, model=self.model)
            return llm
        except Exception as e:
            raise ValueError(f"error in model initial :- {str(e)}")