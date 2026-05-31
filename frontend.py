import streamlit as st
import requests
import time

st.set_page_config(
    page_title="AI Chatbot Agent",
    page_icon="🤖",
    layout="wide"
)

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


# Header

st.markdown(
    '<div class="main-title">🤖 AI Chatbot Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Streamlit + FastAPI + LangGraph AI Assistant</div>',
    unsafe_allow_html=True
)


# Sidebar


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



# Main Container


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


# Backend API URL


API_URL = "https://ai-agent-chatbot-6ntn.onrender.com/chat"


# Ask Button

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


            # Success Response
          
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

       
            # Error Response
         
            else:

                st.error(
                    f"Server Error: {response.status_code}"
                )

                st.code(response.text)

        except Exception as e:

            st.error(f"Connection Error: {str(e)}")

    else:

        st.warning("⚠️ Please enter your query.")


# Footer


st.markdown("---")

st.caption(
    "🚀 Built with Streamlit + FastAPI + LangGraph"
)

