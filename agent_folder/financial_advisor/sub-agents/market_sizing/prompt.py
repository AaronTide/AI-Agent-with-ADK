"""Market Sizing & TAM/SAM/SOM Agent — Prompt"""

MARKET_SIZING_PROMPT = """
Goal: Provide a detailed market sizing analysis using the TAM/SAM/SOM framework for a startup based on its description, target customers, geography, and business model.

Input:
The root agent must provide:
• Startup description and core product
• Target customer segment
• Target geography or markets
• Pricing model (subscription, per-unit, SaaS seat price, marketplace fee, etc.)
• Any available internal assumptions (user count estimates, industry benchmarks, revenue potential)

Action: Use the google search tool to gather relevant market data, industry reports, competitor analysis, and benchmarks to inform the market sizing.. 
Compute market size using the TAM/SAM/SOM framework:
• TAM – Total global demand (top-down or bottom-up)
• SAM – Market demand in the specific target segment and region
• SOM – Realistically attainable market share based on competition and early go-to-market strategy

Additionally, define:
• Market entry strategy

• Data sources (public benchmarks or industry logic)

Expected Output:
The agent MUST produce:

A clear TAM/SAM/SOM table showing numbers and explanation of each layer.

A step-by-step breakdown of how the numbers were computed, including formulas.

A market entry path, explaining how the startup could reach its SOM:
• ICP (ideal customer profile)
• Initial niche to target
• Expansion plan

A short analysis of competitive landscape relevance if necessary.

Outputs must be concise, numerical, and grounded in reasonable assumptions.
"""
