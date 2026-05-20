import asyncio
from dotenv import load_dotenv
load_dotenv()
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from My_first_agent.agent import root_agent

async def chat(message: str):
    # 1. Create a session service (stores conversation history)
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="My_first_agent", user_id="user1"
    )

    # 2. Create a runner (manages the agent execution)
    runner = Runner(
        agent=root_agent,
        app_name="My_first_agent",
        session_service=session_service,
    )

    # 3. Send a message
    msg = Content(parts=[Part(text=message)])

    # 4. Get the response (async generator)
    async for event in runner.run_async(
        user_id="user1",
        session_id=session.id,
        new_message=msg,
    ):
        if event.is_final_response():
            print("Agent:", event.content.parts[0].text)

# Run it!
while True:

    user_input = input("You: ")

    if user_input.lower()== "exit":
        break

    asyncio.run(chat(user_input))