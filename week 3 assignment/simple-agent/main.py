from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("Gemini_API_KEY")
external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key =api_key,
)

set_default_openai_client(external_client)
set_tracing_disabled(True)
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

agent = Agent (
    name="HELLO , World",
    instructions="You are a helpful assistant that Reply in One line only",
    model=model
)

result = Runner.run_sync(agent, "hello in one short sentence.")
print(result.final_output)