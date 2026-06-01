#step1 : setup pydentic model(schema validation)
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends

from database import get_db
from models import User, ChatHistory
from schemas import UserCreate
from auth import hash_password
from schemas import UserLogin
from auth import verify_password
from auth import create_access_token

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from auth import verify_token
from fastapi import HTTPException



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

security = HTTPBearer()


@app.post("/signup")
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:

        return {
            "error": "Email already exists"
        }

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(
            user.password
        )
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }
    
    


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    email = verify_token(token)

    if not email:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return email
@app.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if not existing_user:

        return {
            "error": "Invalid Email"
        }

    if not verify_password(
        user.password,
        existing_user.password
    ):

        return {
            "error": "Invalid Password"
        }

    token = create_access_token(
        {
            "sub": existing_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# @app.post("/chat")
# def chat_endpoint(request: RequestState):
@app.post("/chat")
def chat_endpoint(
    request: RequestState,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)):
    """1. Api endpoint to interact with the chatbot using langGraph and search tools.
       2. it dynamically selects the model specified in the request"""
       
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "invalid model name. kidly select a valid AI model"}
    
    llm_id = request.model_name
    query = request.messages[-1]
    allowed_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
    
    user = (
    db.query(User)
    .filter(User.email == current_user)
    .first()
)
<<<<<<< HEAD

    import time

    start = time.time()

    response = get_response_from_ai_agent(llm_id, query, allowed_search, system_prompt, provider)

    print(
        f"Response Time: {time.time() - start:.2f} sec"
    )

    
=======
    response = get_response_from_ai_agent(llm_id, query, allowed_search, system_prompt, provider)
>>>>>>> 53bb903 (Added JWT authentication, PostgreSQL user management and chat history)
    
    
    chat = ChatHistory(
        user_id=user.id,
        query=query,
        response=response
    )

    db.add(chat)
    db.commit()
    
    return {
        "response":response
    }
    

@app.get("/history")
def get_chat_history(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.email == current_user)
        .first()
    )

    if not user:
        return {"error": "User not found"}

    chats = (
        db.query(ChatHistory)
        .filter(ChatHistory.user_id == user.id)
        .order_by(ChatHistory.created_at.desc())
        .all()
    )

    return chats
    
#step3: run app & explore swagger ui docs
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1", port=9999)