# YouTube Agent Project

## Overview
The YouTube Agent Project is designed to generate structured course outlines in Markdown format from YouTube videos. It leverages AI models and tools to retrieve video transcripts, process them, and create concise and clear course content.

## Features
- **Transcript Retrieval**: Fetches transcripts from YouTube videos in multiple languages.
- **Course Generation**: Converts video transcripts into structured Markdown course outlines.
- **Agent-Based Architecture**: Utilizes sub-agents for specific tasks like video retrieval and course generation.

## Project Structure
```
youtube_agent/
├── __init__.py
├── agent.py
├── .env
├── sub_agents/
│   ├── youtube_course/
│   │   ├── __init__.py
│   │   ├── agent.py
│   ├── youtube_retriever_agent/
│   │   ├── __init__.py
│   │   ├── agent.py
└── requirements.txt
```

- **`agent.py`**: Main agent that coordinates sub-agents.
- **`sub_agents/youtube_course/agent.py`**: Handles course generation from YouTube videos.
- **`sub_agents/youtube_retriever_agent/agent.py`**: Retrieves relevant YouTube videos based on user queries.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd youtube_agent
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. test the project:
   ```bash
   adk web
   ```


## Contributing
Feel free to submit issues or pull requests for improvements.
