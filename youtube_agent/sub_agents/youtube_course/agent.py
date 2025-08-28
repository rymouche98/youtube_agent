import os
import re
from google import genai
from google.adk import Agent
from google.genai.types import Content, Part, FileData
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
load_dotenv()

def get_youtube_transcript(url):
    """
    Fetch the transcript of a YouTube video using its URL.

    Args:
        url (str): The full URL of the YouTube video.

    Returns:
        str: The combined transcript text of the video in the specified languages.

    Raises:
        AttributeError: If the video ID cannot be extracted from the URL.
        youtube_transcript_api.TranscriptsDisabled: If transcripts are disabled for the video.
        youtube_transcript_api.VideoUnavailable: If the video is unavailable.

    Example:
        >>> transcript = get_youtube_transcript("https://www.youtube.com/watch?v=example")
        >>> print(transcript)
        "Transcript text..."
    """
    video_id = re.search(r"(?<=watch\?v=)[\w-]+", url).group(0)
    # Initialize the YouTubeTranscriptApi
    ytt_api = YouTubeTranscriptApi()
    # Fetch the transcript using the correct method
    transcript_obj = ytt_api.fetch(video_id, ['fr','en'])
    # Combine the transcript text
    transcript_txt = ' '.join([part.text for part in transcript_obj.snippets])
    return transcript_txt

def youtube_course_markdown(youtube_link: str) -> str:
    """
    Generate a structured course outline in Markdown from a YouTube video.

    Args:
        youtube_link (str): The full URL of the YouTube video.

    Returns:
        str: A structured course outline in Markdown format, 
             including sections, sub-sections, and bullet points.

    Example:
        >>> md_course = youtube_course_markdown("https://www.youtube.com/watch?v=-otFL1ZD47E")
        >>> print(md_course)
        # Introduction
        - Point 1
        - Point 2
        ...
    """
    client = genai.Client()  # API key assumed in environment
    transcript = get_youtube_transcript(youtube_link)
    prompt = """Please generate a structured course outline from this video transcript in Markdown format. 
                Include sections, subsections, bullet points, and keep it concise and clear."""
    response = client.models.generate_content(
        model='models/gemini-2.5-flash',
        contents=Content(
            parts=[
                Part(
                    text=prompt+transcript
                )
            ]
        )
    )
    return response.text

def youtube_course_markdown_v0(youtube_link: str) -> str:
    """
    Generate a structured course outline in Markdown from a YouTube video.

    Args:
        youtube_link (str): The full URL of the YouTube video.

    Returns:
        str: A structured course outline in Markdown format, 
             including sections, sub-sections, and bullet points.

    Example:
        >>> md_course = youtube_course_markdown("https://www.youtube.com/watch?v=-otFL1ZD47E")
        >>> print(md_course)
        # Introduction
        - Point 1
        - Point 2
        ...
    """
    client = genai.Client()  # API key assumed in environment

    response = client.models.generate_content(
        model='models/gemini-2.5-flash',
        contents=Content(
            parts=[
                Part(
                    file_data=FileData(file_uri=youtube_link)
                ),
                Part(
                    text=(
                        "Please generate a structured course outline from this video in Markdown format. "
                        "Include sections, subsections, bullet points, and keep it concise and clear."
                    )
                )
            ]
        )
    )
    return response.text


youtube_course_agent = Agent(
    name="youtube_course_agent",
    model=os.getenv("MODEL"),
    instruction="Your role is to generate a course from the YouTube video based on the user's request.",
    tools=[youtube_course_markdown]
)
