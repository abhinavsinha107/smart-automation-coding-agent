import asyncio
from dotenv import load_dotenv
from client.llm_client import LLMClient

load_dotenv()


async def main():
    client = LLMClient()
    messages = [{"role": "user", "content": "What's up"}]
    async for event in client.chat_completion(messages, True):
        print(event)
    print("Done")


asyncio.run(main())
