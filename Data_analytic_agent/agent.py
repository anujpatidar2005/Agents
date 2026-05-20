from google.adk.agents import LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor

root_agent = LlmAgent(
    name="data_analyst_agent",

    model="gemini-3-flash-preview",

    description="A data analyst that can write and execute Python code.",

    instruction="""
You are a data analyst. You can:

- Write Python code to analyze data
- Create calculations and statistics
- Solve math problems by running code
- Generate data visualizations
- Always run code to verify answers before presenting them
""",

    code_executor=BuiltInCodeExecutor(),
)