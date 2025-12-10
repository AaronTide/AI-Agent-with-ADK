# FINSTART- FINANCIAL ADVISOR AGENT FOR STARTUPS
### Built using Google ADK 


The Financial Advisor Agent acts as a specialized financial team for a startup founder. 

It orchestrates a series of expert subagents namely- data_analyst_agent, fundraising_agent and grant_funding_agent.
First, it asks the user for necessary information about their startup context and what they need help with.
According to the founder's answer, it can help them analyze a market ticker (which can belong to their own startup or a competitor) 
or develop fundraising strategies for the startup 
or find grants/ funding opportunities according to the startup profile.

## Agent Structure
<img width="656" height="240" alt="image" src="https://github.com/user-attachments/assets/43391806-cd3f-42b0-ae41-524889752ab4" />



## Requirements:

Python 3.14.0 or above

Gemini API Key from Google AI Studio (https://aistudio.google.com/apps)

## Setup Guide

1 )  To see the agents on your own device, use the following commands,

    git clone https://github.com/AaronTide/AI-Agent-with-ADK.git

    cd AI-Agent-with-ADK

    cd agent_folder

2 ) Create and activate .venv

    python -m venv .venv
for Windows

    .venv\Scripts\activate

On macOS/Linux:

    source venv/bin/activate


3 ) Rename ALL .env.example files as .env and put in your Gemini API key 

    GOOGLE_API_KEY=<Your api key here>

4 ) Install Google ADK
    
    pip install google-adk

5 ) Run the agents on web interface
   
    adk web
   
## Sample Conversation 

<img width="1366" height="652" alt="Screenshot (142)" src="https://github.com/user-attachments/assets/d4618fb8-e1bb-4a18-80ce-9f2a7f5d2145" />

