"""GRant funding  Agent for looking up govt/non-govt grants and funding opportunities related to startup """

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL="gemini-2.5-pro"

grant_funding_agent = Agent(
    model=MODEL,
    name="grant_funding_agent",
    instruction=prompt.GRANT_FUNDING_PROMPT,
    output_key="grant_funding_output",
    tools=[google_search],
)
