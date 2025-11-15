from fastapi import APIRouter, Response, HTTPException
from fastapi.responses import JSONResponse
from src.api.schema import BlogRequest
from src.llm import GroqLLM
from src.graphs import GraphBuilder
from src.api.schema import BlogResponse
from pydantic import ValidationError

blog_route = APIRouter(prefix="/blog")

@blog_route.post("/", response_model=BlogResponse)
async def generate_blog(*, blog_in:BlogRequest):
    try:
        blog_in_data = blog_in.model_dump()
        print(f"*** request data {blog_in_data}")

        #  get llm
        groq_ob = GroqLLM()
        llm_model = groq_ob.get_model()

        # graph
        topic = blog_in_data.get("topic")
        language = blog_in_data.get("language")
        use_case = blog_in_data.get("use_case")

        graph_obj = GraphBuilder(llm_model=llm_model)
        graph = graph_obj.setup_graph(use_case)
        response = graph.invoke({"topic": topic, "language":language, "use_case":use_case})
        return response
    
    except ValidationError as ve:
        error_details = ve.errors()
        print(f"*** Validation Error blog post: {error_details}")
        raise HTTPException(
            status_code=422,
            detail={
                "message": "Validation error in request",
                "errors": error_details
            }
        )
    # except Exception as e:
    #     print(f"*** Error blog post: {str(e)}")
    #     raise HTTPException(
    #         status_code=500,
    #         detail={
    #             "message": "Internal server error",
    #             "error": str(e)
    #         }
    #     )

