#step1 : setup API keys for groq, openAi and tavily

import os 

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

#step2 : setup LLM & tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm = ChatOpenAI(model= "gpt-4.1 mini")
groq_llm = ChatGroq(model= "llama-3.3-70b-versatile")

search_tool = TavilySearchResults(max_results = 2)


#step3 : setup AI agent with search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage
# system_prompt = """You are a smart and friendly AI assistant.

# Use web search only for:
# - latest news
# - current events
# - live data
# - recent AI trends
# - crypto prices

# For normal/general knowledge questions,
# answer directly without using tools."""

def get_response_from_ai_agent(llm_id, query, allowed_search ,system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model = llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    
    else:
        raise ValueError("invalid provider selected")
        
    tools = [TavilySearchResults(max_results = 2)] if allowed_search else []
    agent = create_react_agent(
        model = llm,
        tools = tools,
        prompt = system_prompt,
    )

        
    state = {"messages":[("user", query)] }
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]