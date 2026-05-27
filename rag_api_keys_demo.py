import os

def set_api_keys():
    os.environ["LANGSMITH_TRACING"] = "false"
    os.environ["LANGCHAIN_TRACING_V2"] = "false"
    os.environ.pop("LANGSMITH_API_KEY", None)
    os.environ.pop("LANGCHAIN_API_KEY", None)
    os.environ.pop("LANGSMITH_PROJECT", None)
    os.environ.pop("LANGCHAIN_PROJECT", None)

    os.environ['LANGCHAIN_API_KEY'] = "<your-api-key>"
    os.environ['OPENAI_API_KEY'] = "<your-api-key>"
    os.environ['COHERE_API_KEY'] = "<your-api-key>"