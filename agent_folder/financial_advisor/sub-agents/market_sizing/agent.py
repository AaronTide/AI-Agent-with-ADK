"""Market sizing Agent for providing the info about Market Sizing & TAM/SAM/SOM"""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL="gemini-2.5-pro"

market_sizing_agent = Agent(
    model=MODEL,
    name="market_sizing_agent",
    instruction=prompt.MARKET_SIZING_PROMPT,
    output_key="market_assessment_output",
    tools=[google_search],
)
