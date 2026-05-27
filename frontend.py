# =========================================
# AI Agent Chatbot UI
# Streamlit + FastAPI + LangGraph
# =========================================

import streamlit as st
import requests
import time

# =========================================
# Page Config
# =========================================

st.set_page_config(
    page_title="AI Chatbot Agent",
    page_icon="🤖",
    layout="wide"
)

# =========================================
# Custom CSS
# =========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}

.chat-box {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
    margin-top: 20px;
}

.response-box {
    background-color: #0f172a;
    padding: 18px;
    border-radius: 12px;
    border-left: 5px solid #38bdf8;
    margin-top: 15px;
    color: white;
    font-size: 16px;
}

.stButton button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    border: none;
}

.stTextArea textarea {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# Header
# =========================================

st.markdown(
    '<div class="main-title">🤖 AI Chatbot Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Streamlit + FastAPI + LangGraph AI Assistant</div>',
    unsafe_allow_html=True
)

# =========================================
# Sidebar
# =========================================

with st.sidebar:

    st.title("⚙️ Agent Settings")

    st.markdown("---")

    MODEL_NAMES_GROQ = [
        "llama-3.3-70b-versatile",
        "mixtral-8x7b-32768"
    ]

    MODEL_NAMES_OPENAI = [
        "gpt-4o-mini",
        "gpt-4.1-mini"
    ]

    provider = st.radio(
        "Select Provider",
        ["Groq", "OpenAI"]
    )

    if provider == "Groq":

        selected_model = st.selectbox(
            "Select Groq Model",
            MODEL_NAMES_GROQ
        )

    else:

        selected_model = st.selectbox(
            "Select OpenAI Model",
            MODEL_NAMES_OPENAI
        )

    allow_web_search = st.checkbox("🌐 Allow Web Search")

    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

#    info(
#         "This AI Agent uses LangGraph + FastAPI backend."
#     )

# ====== st.===================================
# Main Container
# =========================================

with st.container():

    st.markdown('<div class="chat-box">', unsafe_allow_html=True)

    # System Prompt
    system_prompt = st.text_area(
        "🧠 Define your AI Agent",
        height=100,
        placeholder="You are a helpful AI assistant..."
    )

    # User Query
    user_query = st.text_area(
        "💬 Enter your Query",
        height=150,
        placeholder="Ask Anything..."
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================
# Backend API URL
# =========================================

API_URL = "https://ai-agent-chatbot-6ntn.onrender.com/chat"

# =========================================
# Ask Button
# =========================================

if st.button("🚀 Ask AI Agent"):

    if user_query.strip():

        payload = {
            "model_name": str(selected_model),
            "model_provider": str(provider),
            "system_prompt": str(system_prompt),
            "messages": [str(user_query)],
            "allow_search": bool(allow_web_search)
        }

        try:

            with st.spinner("🤖 AI is thinking..."):

                response = requests.post(
                    API_URL,
                    json=payload,
                    headers={
                        "Content-Type": "application/json"
                    }
                )

                time.sleep(1)

            # =========================================
            # Success Response
            # =========================================

            if response.status_code == 200:

                response_data = response.json()

                if "error" in response_data:

                    st.error(response_data["error"])

                else:

                    st.markdown("## 🤖 AI Response")

                    st.markdown(
                        f'''
                        <div class="response-box">
                        {response_data["response"]}
                        </div>
                        ''',
                        unsafe_allow_html=True
                    )

            # =========================================
            # Error Response
            # =========================================

            else:

                st.error(
                    f"Server Error: {response.status_code}"
                )

                st.code(response.text)

        except Exception as e:

            st.error(f"Connection Error: {str(e)}")

    else:

        st.warning("⚠️ Please enter your query.")

# =========================================
# Footer
# =========================================

st.markdown("---")

st.caption(
    "🚀 Built with Streamlit + FastAPI + LangGraph"
)
# #step1 : steup ui with streamlit(model provider, model,system prompt,quary, web sreach)
# import streamlit as st
# import requests
# import time
# from datetime import datetime

# st.set_page_config(page_title="AI Agent Chatbot",
#     page_icon="🤖",
#     layout="wide",
#     initial_sidebar_state="expanded")
# st.markdown("""
# <style>

# .stApp{
#     background: linear-gradient(to right, #0f172a, #1e293b);
#     color: white;
# }

# .main{
#     color: white;
# }

# .title-style{
#     text-align:center;
#     font-size:42px;
#     font-weight:bold;
#     color:#38bdf8;
#     margin-bottom:10px;
# }

# .subtitle-style{
#     text-align:center;
#     color:#cbd5e1;
#     margin-bottom:30px;
# }

# .chat-user{
#     background-color:#2563eb;
#     padding:14px;
#     border-radius:12px;
#     margin:10px 0px;
#     color:white;
#     font-size:16px;
# }

# .chat-bot{
#     background-color:#1e293b;
#     padding:14px;
#     border-radius:12px;
#     margin:10px 0px;
#     border:1px solid #334155;
#     color:white;
#     font-size:16px;
# }

# .stButton button{
#     width:100%;
#     border-radius:10px;
#     height:50px;
#     background-color:#2563eb;
#     color:white;
#     font-size:18px;
#     border:none;
# }

# .stTextArea textarea{
#     border-radius:10px;
# }

# </style>
# """, unsafe_allow_html=True)


# # system_prompt = st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here....")

# with st.sidebar:

#     st.title("⚡ AI Agent Settings")

#     st.markdown("---")

#     MODEL_NAMES_GROQ = [
#         "llama-3.3-70b-versatile",
#         "mixtral-8x7b-32768"
#     ]

#     MODEL_NAMES_OPENAI = [
#         "gpt-4o-mini",
#         "gpt-4.1-mini"
#     ]

#     provider = st.radio(
#         "Select Provider",
#         ["Groq", "OpenAI"]
#     )

#     if provider == "Groq":
#         selected_model = st.selectbox(
#             "Select Groq Model",
#             MODEL_NAMES_GROQ
#         )

#     else:
#         selected_model = st.selectbox(
#             "Select OpenAI Model",
#             MODEL_NAMES_OPENAI
#         )

#     allow_web_search = st.checkbox("🌐 Allow Web Search")

#     st.markdown("---")

#     if st.button("🗑️ Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()
        
    
# st.markdown(
#     '<div class="title-style">🤖 AI Agent Chatbot</div>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<div class="subtitle-style">Smart AI Assistant using Streamlit + FastAPI + LangGraph</div>',
#     unsafe_allow_html=True
# )

# if "messages" not in st.session_state:
#     st.session_state.messages = []
    
# for message in st.session_state.messages:

#     if message["role"] == "user":

#         st.markdown(
#             f"""
#             <div class="chat-user">
#             <b>🧑 You:</b><br>
#             {message["content"]}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#     else:

#         st.markdown(
#             f"""
#             <div class="chat-bot">
#             <b>🤖 AI:</b><br>
#             {message["content"]}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# user_query = st.text_area("Enter your query: ", height=150 , placeholder="Ask Anything!")

# # user_query = st.chat_input("💬 Ask Anything...")

# #step2: connect with backend vie URL
# API_URL="http://127.0.0.1:9999/chat"



# if user_query:
#     st.session_state.messages.append({
#         "role": "user",
#         "content": user_query
#     })

#     # Show User Message
#     st.markdown(
#         f"""
#         <div class="chat-user">
#         <b>🧑 You:</b><br>
#         {user_query}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
#     with st.spinner("🤖 AI is thinking..."):
        
#         payload ={
#             "model_name": selected_model,
#             "model_provider": provider,
#             # "system_prompt": system_prompt,
#             "messages": [user_query],
#             "allow_search": allow_web_search
#         }
        
#     response = requests.post(API_URL, json=payload)
#     if response.status_code==200:
#             response_data = response.json()
#             if "error" in response_data:
#                 st.error(response_data["error"])
            
#             # else:
#             #     st.subheader("Agent Response")
#             #     st.markdown(f"**final Response :** {response_data['response']}")
                
#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": response
#     })

#     # Show AI Response
#     st.markdown(
#         f"""
#         <div class="chat-bot">
#         <b>🤖 AI:</b><br>
#         {response}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# st.markdown("---")

# current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# st.caption(
#     f"🚀 AI Agent Chatbot | Streamlit Frontend | {current_time}"
# )
