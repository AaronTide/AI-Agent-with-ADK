The Financial Advisor Agent acts as a specialized financial advisor for a startup founder. 

It orchestrates a series of expert subagents namely- data_analyst_agent, fundraising_agent and grant_funding_agent.
First, it asks the user for necessary information about their startup context and what they need help with.
According to the founder's answer, it can help them analyze a market ticker (which can belong to their own startup or a competitor) 
or develop fundraising strategies for the startup 
or find grants/ funding opportunities according to the startup profile.

Requirements: 

Python 3.14.0 or above

Gemini API Key from Google AI Studio (https://aistudio.google.com/apps)

1 )  To see the agents on your own device, use the following commands,

    git clone https://github.com/AaronTide/AI-Agent-with-ADK.git

    cd AI-Agent-with-ADK

    cd agent_folder

2 ) Create and activate .venv

    python -m venv .venv
      
    .venv\Scripts\activate


3 ) Rename ALL .env.example files as .env and put in your Gemini API key 

    GOOGLE_API_KEY=<Your api key here>

4 ) Install Google ADK
    
    pip install google-adk

5 ) Run the agents on web interface
   
    adk web
   




   

    

