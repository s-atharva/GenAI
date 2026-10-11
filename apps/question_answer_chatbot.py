from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
import streamlit as st

llm = ChatGroq(
    model = 'openai/gpt-oss-120b'
)

st.title('Question and Answer Chatbot')
st.markdown("""
            QnA Bot with Groq
            """)

if "messages" not in st.session_state: 
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message['role']
    content = message['content']
    st.chat_message(role).markdown(content)
    

query = st.chat_input("Ask anything: ")
if query:
    st.session_state.messages.append({'role': 'user', 'content': query})
    st.chat_message('user').markdown(query)
    response = llm.invoke(query)
    st.chat_message('ai').markdown(response.content)
    st.session_state.messages.append({'role': 'ai', 'content': response.content})
    