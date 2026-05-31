# 🤖 AI Agent Chatbot

Built an AI-powered chatbot using LangGraph, LangChain, FastAPI, and Streamlit to deliver intelligent and context-aware conversations.
Implemented the ReAct Agent architecture, enabling the chatbot to reason through queries and use external tools when needed.
Integrated OpenAI and Groq LLMs with dynamic model selection, allowing users to switch between models based on their requirements.
Added real-time web search functionality to provide up-to-date and accurate responses beyond the model's knowledge base.
Developed RESTful APIs with FastAPI and managed agent workflows using LangGraph for smooth and efficient query processing.
Created a clean and interactive Streamlit interface, making it easy for users to interact with the chatbot and view responses in real time
## 🚀 Live Demo

🔗 Live App: https://aiagentchatbot-fortesting.streamlit.app/

🔗 Backend API: https://ai-agent-chatbot-6ntn.onrender.com

## 📌 Features

- 🧠 ReAct Agent Architecture
- 🔍 Real-Time Web Search Integration
- 🤖 Multiple LLM Support
  - OpenAI
  - Groq
- 🔄 Dynamic Model Selection
- ⚡ FastAPI Backend APIs
- 🎨 Streamlit Frontend
- 💬 Interactive Chat Interface
- 📚 LangGraph Workflow Management
- 🛠 Tool Calling Support
- 🌐 External Information Retrieval

## 🏗 Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Python

### AI Frameworks
- LangChain
- LangGraph

### LLM Providers
- OpenAI
- Groq

### Search Tools
- Tavily Search API

## 📂 Project Structure

```bash
AI_Agent_Chatbot/
│
├── frontend/
├── backend/
├── agents/
├── tools/
├── api/
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/vibhanshu007-tpo/AI_Agent_Chatbot.git

cd AI_Agent_Chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```

## ▶️ Run FastAPI Backend

```bash
uvicorn main:app --reload
```

## ▶️ Run Streamlit Frontend

```bash
streamlit run app.py
```

## 🧠 How It Works

1. User sends a query.
2. LangGraph manages workflow execution.
3. ReAct Agent decides whether tools are required.
4. Tavily Search retrieves external information if needed.
5. Selected LLM generates the response.
6. Response is displayed through Streamlit UI.




## 🔮 Future Improvements

- Authentication System
- Chat History Storage
- RAG Integration
- Voice Assistant Support
- Multi-Agent Collaboration
- Docker Deployment

## 👨‍💻 Author

**Vibhanshu Hirapure**

GitHub:
https://github.com/vibhanshu007-tpo

LinkedIn:
https://www.linkedin.com/in/vibhanshu-hirapure/


## 📄 License

This project is licensed under the MIT License.
