from google.adk.agents import LlmAgent        # Llm genimi ka hi brain use krega or agent sb ka
#from google.adk.tools import google_search

root_agent = LlmAgent(
    name= "my_first_agent",
    model="gemini-3-flash-preview",
    description="An example agent that will answer users query,If can not give answer clearly inform users",
    instruction="""
    you are a chef , you have to tell people how to make a "KADAK MASALE WALI CHAI" from beginning in a polite and simple 
    way in short and brief . also support with positive emojies and also solve queries releted to recipe. 
    """,
    #tools =[google_search]
)