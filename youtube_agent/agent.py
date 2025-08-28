from google.adk import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv
from youtube_agent.sub_agents.youtube_course.agent import youtube_course_agent
from youtube_agent.sub_agents.youtube_retriever_agent.agent import youtube_retriever_agent
import os

load_dotenv()

prompt = """When a question concerns generating a course from a YouTube video or a given topic, follow this logic:  
        1. If the user provides a topic or subject, first use the `youtube_retriever_agent` tool to find a relevant video matching the topic, then send the retrieved link to `youtube_course_agent`.  
        2. If the user provides a YouTube link, pass it directly to the `youtube_course_agent` tool to generate the course in Markdown.  
        3. The generated course should be structured in Markdown with:  
        - Sections (#)  
        - Subsections (##)  
        - Key points (-)  
        4. Ensure the Markdown is clear, readable, and ready to be exported or displayed.
        """

root_agent = Agent(
    name="main_root_agent",
    model=os.getenv("MODEL"),
    instruction=prompt,
    sub_agents=[youtube_retriever_agent, youtube_course_agent]
)