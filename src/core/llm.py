from langchain_groq import ChatGroq
from . import settings

llm = ChatGroq(model_name="openai/gpt-oss-120b", api_key=settings.GROQ_API_KEY)