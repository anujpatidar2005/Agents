# Data Analytics Agent

An AI-powered data analyst agent built using Google Agent 
Development Kit (ADK) and Gemini LLM.

## What it does
- Writes and executes Python code automatically
- Performs data analysis and statistical calculations
- Solves math problems by running code in real-time
- Generates data visualizations
- Verifies all answers by executing code before responding

## Technologies Used
- Python
- Google ADK (Agent Development Kit)
- Gemini LLM (gemini-flash)
- BuiltInCodeExecutor

## How to Run

1. Install dependencies:
   pip install google-adk

2. Set up Gemini API key:
   GOOGLE_API_KEY=your_api_key_here

3. Run the agent:
   python agent.py

## Project Structure
data_analytic_agent/
│
├── agent.py        # Main agent code
└── README.md       # Project info
