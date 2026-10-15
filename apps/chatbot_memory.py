from http.client import responses

from dotenv import load_dotenv

load_dotenv()

# llm + memory + agent
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

llm = ChatGroq(
    model='openai/gpt-oss-120b'
)

agent = create_agent(
    model=llm,
    tools=[],
    checkpointer=InMemorySaver(),
    system_prompt="You are an amazing AI assistant."
)

config = {
    'configurable': {
        'thread_id': 'M1'
    }
}

while True:
    user_input = input("User: ")
    if user_input.lower() in ['exit', 'thank you', 'bye']:
        print('GoodBye')
        break

    response = agent.invoke({
        'messages': {
            'role': 'user',
            'content': user_input
        }
    },
        config=config
    )

    result = response['messages'][-1].content
    print(f'AI: {result}')
    print()
