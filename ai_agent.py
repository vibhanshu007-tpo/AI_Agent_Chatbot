import os
<<<<<<< HEAD
from functools import lru_cache
=======
>>>>>>> 53bb903 (Added JWT authentication, PostgreSQL user management and chat history)
from dotenv import load_dotenv

load_dotenv()

<<<<<<< HEAD
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

=======
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

#step2 : setup LLM & tools

>>>>>>> 53bb903 (Added JWT authentication, PostgreSQL user management and chat history)
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
<<<<<<< HEAD
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage


@lru_cache(maxsize=20)
def get_cached_agent(
    llm_id,
    provider,
    system_prompt
):
    if provider == "Groq":
=======

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

>>>>>>> 53bb903 (Added JWT authentication, PostgreSQL user management and chat history)
        llm = ChatGroq(
            model=llm_id,
            api_key=GROQ_API_KEY
        )

    elif provider == "OpenAI":
<<<<<<< HEAD
=======

>>>>>>> 53bb903 (Added JWT authentication, PostgreSQL user management and chat history)
        llm = ChatOpenAI(
            model=llm_id,
            api_key=OPENAI_API_KEY
        )

    else:
<<<<<<< HEAD
        raise ValueError("Invalid provider")

    tools = [
        TavilySearchResults(max_results=1)
    ]

    return create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )


def get_llm(
    llm_id,
    provider
):
    if provider == "Groq":
        return ChatGroq(
            model=llm_id,
            api_key=GROQ_API_KEY
        )

    elif provider == "OpenAI":
        return ChatOpenAI(
            model=llm_id,
            api_key=OPENAI_API_KEY
        )

    raise ValueError("Invalid provider")


def get_response_from_ai_agent(
    llm_id,
    query,
    allowed_search,
    system_prompt,
    provider
):
    try:

        # FAST PATH
        if not allowed_search:

            llm = get_llm(
                llm_id,
                provider
            )

            messages = []

            if system_prompt:
                messages.append(
                    (
                        "system",
                        system_prompt
                    )
                )

            messages.append(
                (
                    "human",
                    query
                )
            )

            response = llm.invoke(messages)

            return response.content

        # SEARCH PATH
        agent = get_cached_agent(
            llm_id,
            provider,
            system_prompt
        )

        response = agent.invoke(
            {
                "messages": [
                    ("user", query)
                ]
            },
            config={
                "recursion_limit": 10
            }
        )

        ai_messages = [
            msg.content
            for msg in response["messages"]
            if isinstance(msg, AIMessage)
=======
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
>>>>>>> 53bb903 (Added JWT authentication, PostgreSQL user management and chat history)
        ]

        return ai_messages[-1]

    except Exception as e:
<<<<<<< HEAD
        return f"Error: {str(e)}"
# import os
# from dotenv import load_dotenv

=======

        return f"Error: {str(e)}"
    
    
# #step1 : setup API keys for groq, openAi and tavily

# import os 
# from dotenv import load_dotenv
>>>>>>> 53bb903 (Added JWT authentication, PostgreSQL user management and chat history)
# load_dotenv()

# GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
<<<<<<< HEAD
# GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# #step2 : setup LLM & tools

# from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.tools.tavily_search import TavilySearchResults

# #step3 : setup AI agent with search tool functionality

# from langgraph.prebuilt import create_react_agent
# from langchain_core.messages import AIMessage

# def get_response_from_ai_agent(
#     llm_id,
#     query,
#     allowed_search,
#     system_prompt,
#     provider
# ):

#     if provider == "Groq":

#         llm = ChatGroq(
#             model=llm_id,
#             api_key=GROQ_API_KEY
#         )

#     elif provider == "OpenAI":

#         llm = ChatOpenAI(
#             model=llm_id,
#             api_key=OPENAI_API_KEY
#         )

#     else:
#         raise ValueError("Invalid provider selected")

#     tools = [
#         TavilySearchResults(max_results=2)
#     ] if allowed_search else []

#     # Create Agent
#     agent = create_react_agent(
#         model=llm,
#         tools=tools,
#         prompt=system_prompt,
#     )

#     state = {
#         "messages": [("user", query)]
#     }

#     try:

#         response = agent.invoke(
#             state,
#             config={
#                 "recursion_limit": 20
#             }
#         )

#         messages = response.get("messages")

#         ai_messages = [
#             message.content
#             for message in messages
#             if isinstance(message, AIMessage)
#         ]

#         return ai_messages[-1]

#     except Exception as e:

#         return f"Error: {str(e)}"
=======

# #step2 : setup LLM & tools
# from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI
# from langchain_community.tools.tavily_search import TavilySearchResults

# openai_llm = ChatOpenAI(model= "gpt-4o-mini")
# groq_llm = ChatGroq(model= "llama-3.3-70b-versatile")

# search_tool = TavilySearchResults(max_results = 2)


# #step3 : setup AI agent with search tool functionality
# from langgraph.prebuilt import create_react_agent
# from langchain_core.messages import AIMessage
# # system_prompt = """You are a smart and friendly AI assistant.

# # Use web search only for:
# # - latest news
# # - current events
# # - live data
# # - recent AI trends
# # - crypto prices

# # For normal/general knowledge questions,
# # answer directly without using tools."""

# def get_response_from_ai_agent(llm_id, query, allowed_search ,system_prompt, provider):
#     if provider == "Groq":
#         llm = ChatGroq(
#                 model=llm_id,
#                 api_key=GROQ_API_KEY
#             )
#     elif provider == "OpenAI":
#         llm = ChatOpenAI(
#                 model=llm_id,
#                 api_key=OPENAI_API_KEY
#             )
    
#     else:
#         raise ValueError("invalid provider selected")
        
#     tools = [TavilySearchResults(max_results = 2)] if allowed_search else []
#     # agent = create_react_agent(
#     #     model = llm,
#     #     tools = tools,
#     #     prompt = system_prompt,
#     # )
#     # response = llm.invoke(query)
#     # print(response.content)
        
#     # state = {"messages":[("user", query)] }
#     # response = agent.invoke(state)
#     # messages = response.get("messages")
#     # ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
#     # return ai_messages[-1]
    
#     state = {
#     "messages": [("user", query)]
# }

#     response = agent.invoke(
#         state,
#         config={
#         "recursion_limit": 3
#     }
# )

#     messages = response.get("messages")

#     ai_messages = [
#         message.content
#         for message in messages
#         if isinstance(message, AIMessage)
#     ]

#     return ai_messages[-1]


#step1 : setup API keys for groq, openAi and tavily
>>>>>>> 53bb903 (Added JWT authentication, PostgreSQL user management and chat history)
