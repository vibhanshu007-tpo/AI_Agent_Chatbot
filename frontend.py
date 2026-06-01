import streamlit as st
import requests
import time

if "messages" not in st.session_state:
    st.session_state.messages = []

if "token" not in st.session_state:
    st.session_state.token = None

if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "Login"

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
# Login Function
# =========================================



def show_auth_page():

    st.subheader("🔐 Authentication")

    
    auth_mode = st.radio(
        "Choose Option",
        ["Login", "Signup"],
        index=0 if st.session_state.auth_mode == "Login" else 1
    )

    if auth_mode == "Signup":

        name = st.text_input("Name")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Create Account"):

            payload = {
                "name": name,
                "email": email,
                "password": password
            }

            response = requests.post(
                "http://127.0.0.1:9999/signup",
                json=payload
            )

            data = response.json()

            if "message" in data:

                st.success(
                    "Account Created Successfully"
                )

                # st.session_state.auth_mode = "Login"
                st.success("account created successfully")

                st.rerun()

            else:

                st.error(
                    data.get(
                        "error",
                        "Signup Failed"
                    )
                )

    else:

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            payload = {
                "email": email,
                "password": password
            }

            response = requests.post(
                "http://127.0.0.1:9999/login",
                json=payload
            )

            if response.status_code == 200:
                

                data = response.json()

                if "access_token" in data:

                    st.session_state.token = (
                        data["access_token"]
                    )

                    st.success(
                        "Login Successful"
                    )

                    st.rerun()
            else:
                st.error("Invalid Email or password")
                    
if not st.session_state.token:

    show_auth_page()

    st.stop()
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
        
    st.markdown("## 📜 Previous Chats")

    user_messages = [
        msg for msg in st.session_state.messages
        if msg["role"] == "user"
    ]

    for msg in reversed(user_messages):

        st.markdown(
            f"🔹 {msg['content'][:35]}"
        )
    
    
    st.markdown("---")

    if st.button("🚪 Logout"):

        st.session_state.clear()

        st.rerun()

#    info(
#         "This AI Agent uses LangGraph + FastAPI backend."
#     )

# ====== st.===================================
# Main Container
# =========================================
# if st.session_state.messages:

#     st.markdown("## 💬 Chat History")

#     for message in st.session_state.messages:

#         if message["role"] == "user":

#             st.markdown(
#                 f"**🧑 You:** {message['content']}"
#             )

#         else:

#             st.markdown(
#                 f"**🤖 AI:** {message['content']}"
#             )

#         st.markdown("---")
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
API_URL = "http://127.0.0.1:9999/chat"
# API_URL = "https://ai-agent-chatbot-6ntn.onrender.com"

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
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {st.session_state.token}"
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
                    
                    st.session_state.messages.append(
                        {
                            "role": "user",
                            "content": user_query
                        }
                    )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": response_data["response"]
                        }
                    )
                    
                

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