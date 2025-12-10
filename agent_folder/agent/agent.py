from google.adk.agents import Agent
from google.adk.tools import google_search 
from datetime import datetime


def get_current_time() -> dict:
    """"Get current time in format: YYYY-MM-DD HH:MM:SS"""

    return{
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        
    
    }

root_agent=Agent(
    name="basic_time_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions using tool: get_current_time",
    instruction="you are a helpful assistant. answer the user's question using tool: get_current_time",
    # tools=[google_search],
    tools=[get_current_time],
)
