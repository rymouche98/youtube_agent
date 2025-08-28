from google.adk import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv
import os

load_dotenv()

youtube_retriever_agent = Agent(
    name="youtube_retriever_agent",
    model=os.getenv("MODEL"),
    instruction="Your role is to retrieve the best YouTube videos based on the user's request using the google_search tool.",
    tools=[google_search]
)
