"""Financial coordinator: provide insights on startup/ competitor's market shares & stocks and strategy for fundraising of startup."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.data_analyst import data_analyst_agent
from .sub_agents.fundraising_analyst import fundraising_analyst_agent

from .sub_agents.grant_funding import grant_funding_agent

#from .sub_agents.risk_analyst import risk_analyst_agent
#from .sub_agents.trading_analyst import trading_analyst_agent


MODEL = "gemini-2.5-pro"


financial_coordinator = LlmAgent(
    name="financial_coordinator",
    model=MODEL,
    description=(
        "guide startup founders through a structured process to receive financial "
        "advice by orchestrating a series of expert subagents. "
        " Get relevant information about their startup and help them "
        "analyze a market ticker for their startup/ provided company"
         "and develop fundraising strategies for the startup"
         "and also find relevant grants and funding opportunities according to startup profile"
        
    ),
    instruction=prompt.FINANCIAL_COORDINATOR_PROMPT,
    output_key="financial_coordinator_output",
    tools=[
        AgentTool(agent=data_analyst_agent),
        AgentTool(agent=fundraising_analyst_agent),
        AgentTool(agent=grant_funding_agent),

        #AgentTool(agent=grant_funding_agent),
        #AgentTool(agent=execution_analyst_agent),
        #AgentTool(agent=risk_analyst_agent),
    ],
)

root_agent = financial_coordinator
