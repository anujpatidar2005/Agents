# QuizBot — AI-Powered Interactive Quiz Agent

An AI quiz master agent built using Google Agent Development
Kit (ADK) and Gemini LLM that generates dynamic MCQs on
any topic with real-time scoring.

## What it does
- Generates 5 multiple-choice questions on any user-given topic
- Shows ONE question at a time with options A, B, C, D
- Validates answers in real-time and explains why
- Tracks live score (X/5) throughout the quiz
- Gives performance feedback at the end
- Always encouraging — even when answers are wrong!

## Technologies Used
- Python
- Google ADK (Agent Development Kit)
- Gemini LLM (gemini-flash)
- LlmAgent Framework

## How to Run

1. Install dependencies:
   pip install google-adk

2. Set up Gemini API key:
   GOOGLE_API_KEY=your_api_key_here

3. Run the agent:
   python agent.py

## Example Interaction
User: start quiz Python
Bot:  Question 1/5: What is a list in Python?
      A) A number
      B) An ordered collection
      C) A function
      D) A loop

## Project Structure
Quiz_Master_Agent/
│
├── agent.py        # Main agent code
└── README.md       # Project info
