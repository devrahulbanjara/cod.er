from typing import Annotated
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    GROQ_API_KEY: Annotated[str, "API key to use LLMs from Groq"]

    TAVILY_API_KEY: str

    LANGCHAIN_TRACING_V2: bool = True
    LANGCHAIN_ENDPOINT: str
    LANGCHAIN_API_KEY: str
    LANGCHAIN_PROJECT: str

    class Config:
        env_file = ".env"


settings = Settings()
