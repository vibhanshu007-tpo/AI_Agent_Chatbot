import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

#step2 : setup LLM & tools

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults

#step3 : setup AI agent with search tool functionality

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage

def get_response_from_ai_agent(
    llm_id,
    query,
    allowed_search,
    system_prompt,
    provider
):

    if provider == "Groq":

        llm = ChatGroq(
            model=llm_id,
            api_key=GROQ_API_KEY
        )

    elif provider == "OpenAI":

        llm = ChatOpenAI(
            model=llm_id,
            api_key=OPENAI_API_KEY
        )

    else:
        raise ValueError("Invalid provider selected")

    tools = [
        TavilySearchResults(max_results=2)
    ] if allowed_search else []

    # Create Agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt,
    )

    state = {
        "messages": [("user", query)]
    }

    try:

        response = agent.invoke(
            state,
            config={
                "recursion_limit": 20
            }
        )

        messages = response.get("messages")

        ai_messages = [
            message.content
            for message in messages
            if isinstance(message, AIMessage)
        ]

        return ai_messages[-1]

    except Exception as e:

        return f"Error: {str(e)}"