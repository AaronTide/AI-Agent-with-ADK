"""Fundrasing Analyst Agent for providing the strategies for startup fundraising """

from google.adk import Agent
#from google.adk.tools import google_search

from . import prompt

MODEL="gemini-2.5-pro"

fundraising_analyst_agent = Agent(
    model=MODEL,
    name="fundraising_analyst_agent",
    instruction=prompt.FUNDRAISING_ANALYST_PROMPT,
    output_key="fundraising_assessment_output",
    
)
