
from typing import Literal
from src.states import BlogState
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage
from src.states import Blog


class BlogNodes:
    """Blog related nodes. to generate title and content
    """

    def __init__(self, model: ChatGroq):
        """Generate title and content

        Args:
            model (ChatGroq): llm model
        """
        self.model = model

    def node_generate_title(self, state: BlogState):
        """_summary_
        """
        topic = state.get("topic")
        if not topic:
            print("****** topic not found in topic generate *******")
            return state

        prompt = """
           You are an expert title-generation agent. Create a catchy and relevant **single-line title** based on the given topic — similar to a blog headline.

            **Topic:**
            {topic}

           Please format the output using **Markdown**
            """

        chain = self.model | StrOutputParser()
        title = chain.invoke(prompt.format(topic=topic))
        return {"blog": {"title": title}}

    def node_generate_content(self, state: BlogState):
        """_summary_
        """
        topic = state.get("topic")
        if not topic:
            print("****** topic not found in content generate *******")
            return state

        prompt = """
        You are an expert content-generation agent. Create detailed and informative content using only relevant information.
        Include a clear **introduction**, **key points**, and a **conclusion** for the given topic.

        **Topic:**
        {topic}

        Please format the output using **Markdown**.
        """

        chain = self.model | StrOutputParser()
        content = chain.invoke(prompt.format(topic=topic))
        return {**state, "blog": {**state["blog"], "content": content}}

    def node_translate(self, state: BlogState):
        """Translate blog content to specific language.
        asper user requirements
        """

        prompt = ChatPromptTemplate.from_template("""
            You are a professional translator. Your task is to translate.
            The following content, title into the specified language

            **without changing any meaning, structure, formatting, or additional wording**.

            🔒 **Important Instructions:**
            - Do NOT add new information.
            - Do NOT remove or omit anything.
            - Do NOT modify titles, headings, numbers, bullet points, or formatting.
            - Only translate the language — keep everything else EXACTLY the same.
            - Preserve Markdown formatting exactly as it is.

            ---

            **Title to Translate:**
            {title}

            **Content to Translate:**
            {content}

            **Target Language:**
            {language}
            """
        )
        try:
            blog = state["blog"]
            title = blog["title"]
            content = blog["title"]
            target_language = state["language"]
        except KeyError:
             print("****** blog, title, title Key not found in state *******")
             return

        model = self.model.with_structured_output(Blog)

        prompt_value = prompt.format(
            title=title,
            content=content,
            language=target_language
        )

        response = model.invoke(prompt_value)

        return {**state, "blog": response.model_dump()}


    def node_route(self, state: BlogState):
        return {"language": state.get("language")}

    def node_routes_decision(self, state:BlogState)->Literal["french", "hindi", "english"]:
        """route node specific translate node

        Returns:
            str: Route node
        """
        language = state.get("language")
        if language == "french":
            return "french"
        elif language == "hindi":
            return "hindi"
        else:
            return "english"