from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
from dotenv import load_dotenv
from agno.models.groq import Groq
import streamlit as st


load_dotenv()

st.set_page_config(
    page_title="AI YouTube Analyzer",
    page_icon="🎥",
    layout="centered"
)

@st.cache_resource
def getAgent():
    return  Agent(
        model=Groq(id="qwen/qwen3-32b"),
        markdown =True,
        tools=[YouTubeTools(enable_get_video_timestamps=True)],
            description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
            instructions="""
            Analyze YouTube video transcripts and provide:
            - concise summaries
            - key insights
            - important topics
            - technologies/tools mentioned
            - accurate answers based only on transcript content

            Keep responses factual, structured, and beginner-friendly.
            Do not hallucinate information.
            """
                 
    )


agent = getAgent()


st.title('🚀 YouTube Insight Agent')
url = st.text_input(
    'Enter Youtube video URL',
    placeholder='https://youtube.com/watch?v=...'
    )
button = st.button(
            'Analyze',
            use_container_width=True
            )

if button:
    if not url:
        st.warning("Please enter a YouTube URL")

    elif "youtube.com" not in url and "youtu.be" not in url:
        st.warning("Please enter a valid YouTube URL")
    else:
        with st.spinner('Analyzing...'):
            try:
                response = agent.run(f"Analyze this video {url}")
                st.markdown(response.content)

            except Exception as e:
                st.error(f"Error: {e}")
