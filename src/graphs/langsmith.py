"""
Variable that are declared below using for langsmith tracking
 
"""


from src.llm import GroqLLM
from src.graphs import GraphBuilder

"""
Base blog graph ----
"""

llm = GroqLLM().get_model()
graph_obj = GraphBuilder(llm)
graph = graph_obj.build_topic_graph().compile()

"""
Base blog graph ----
"""