# LinguaBot — AI Language Tutor Agent

A patient and encouraging AI language tutor built using 
Google Agent Development Kit (ADK) and Gemini LLM that 
teaches any language interactively.

## What it does
- Teaches vocabulary, grammar, and phrases for any language
- Corrects mistakes gently with detailed explanation
- Creates practice exercises on demand
- Translates words and explains cultural nuances
- Uses spaced repetition to review previously learned words
- Introduces max 5 new words per session — no overwhelm!

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

## Commands You Can Use
| Command | Example |
|---|---|
| Teach me a topic | "Teach me greetings in Japanese" |
| Quiz yourself | "Quiz me on vocabulary" |
| Get corrections | "Correct my sentence: Me want food" |
| Translate | "How do you say thank you in French?" |

## Example Interaction
User: Teach me greetings in Spanish
Bot:  Hola [OH-lah] — Hello
      Example: "Hola, ¿cómo estás?"

## Project Structure
language_agent/
│
├── agent.py        # Main agent code
└── README.md       # Project info
