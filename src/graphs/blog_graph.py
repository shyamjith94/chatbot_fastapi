from langgraph.graph import StateGraph, START, END
from src.states import BlogState
from src.nodes import BlogNodes
from src.core import BlogUseCaseEnum


class GraphBuilder:
    def __init__(self, llm_model):
        """Building Graph. using llm model

        Args:
            llm_model (_type_): pass any llm model
        """
        self.graph = StateGraph(BlogState)
        self.model = llm_model

    def build_topic_graph(self):
        """Create blog and title based on topic 
        """
        nodes = BlogNodes(self.model)
        
        # nodes
        self.graph.add_node("title_creation", nodes.node_generate_title)
        self.graph.add_node("content_creation", nodes.node_generate_content)

        # edges

        self.graph.set_entry_point("title_creation")
        self.graph.add_edge("title_creation", "content_creation")
        self.graph.add_edge("content_creation", END)

        return self.graph # for langsmith

    def build_topic_language_graph(self):
        """user can specify the language they want details
            like content and title 
        """
        nodes = BlogNodes(self.model)
        
        # nodes
        self.graph.add_node("title_creation", nodes.node_generate_title)
        self.graph.add_node("content_creation",nodes.node_generate_content)
        self.graph.add_node("routes", nodes.node_route)
        
        # ---- Translation nodes (language INSIDE state) ----
        self.graph.add_node("hindi_translation",lambda state: nodes.node_translate({**state, "language": "hindi"}))
        self.graph.add_node("french_translation",lambda state: nodes.node_translate({**state, "language": "french"}))
        
        # edges

        self.graph.set_entry_point("title_creation")
        self.graph.add_edge("title_creation", "content_creation")
        self.graph.add_edge("content_creation", "routes")
        self.graph.add_conditional_edges("routes", 
                                        nodes.node_routes_decision,
                                        {"french":"french_translation", "hindi":"hindi_translation"})
        self.graph.add_edge("french_translation", END)
        self.graph.add_edge("hindi_translation", END)

        return self.graph # for langsmith


    def setup_graph(self, use_case: str):
        try:
            use_case = BlogUseCaseEnum(use_case)

            match use_case:
                case BlogUseCaseEnum.GENERATE_BLOG:
                    self.build_topic_graph()
                case BlogUseCaseEnum.GENERATE_TRANSLATE:
                    self.build_topic_language_graph()
                case _:
                    raise ValueError("Use case not found ")
            return self.graph.compile()
        except ValueError:
            print(f"******** Use case not found ****")