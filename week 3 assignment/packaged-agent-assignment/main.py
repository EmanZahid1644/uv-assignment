from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, set_default_openai_client
from dotenv import load_dotenv
import os

load_dotenv()  # <-- yeh line add karo

api_key = os.getenv("Gemini_API_KEY")
external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)
set_default_openai_client(external_client)
set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)
agent = Agent(
    name="Hello, World",
    instructions="You are a very friendly assistant that replies in one line only.",
    model=model
)
result = Runner.run_sync(agent, "Greet the user in one line")
print(result.final_output)
