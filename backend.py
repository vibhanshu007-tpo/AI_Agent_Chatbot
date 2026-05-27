#step1 : setup pydentic model(schema validation)
from pydantic import BaseModel
from typing import List
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

#step2: setup AI agent form frontend request

from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent
ALLOWED_MODEL_NAMES = ["llama3-70b-8192","mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4.1-mini","gpt-4o-mini"]
app = FastAPI(title="langGraph AI agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """1. Api endpoint to interact with the chatbot using langGraph and search tools.
       2. it dynamically selects the model specified in the request"""
       
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "invalid model name. kidly select a valid AI model"}
    
    llm_id = request.model_name
    query = request.messages[-1]
    allowed_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
    response = get_response_from_ai_agent(llm_id, query, allowed_search, system_prompt, provider)
    return {
        "response":response
    }
    
#step3: run app & explore swagger ui docs
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1", port=9999)