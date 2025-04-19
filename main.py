# PythonAIAgentClaude - A Research Assistant using LangChain and Anthropic's Claude
# Developed by: Jason Jiwan
# Date: April 2025
# Description: This project uses LangChain with Claude to research user queries, leveraging tools
# like Wikipedia and DuckDuckGo search, and saves responses to a text file.

from dotenv import load_dotenv
import os
import re
import json
from datetime import datetime
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

# Load environment variables
load_dotenv(verbose=True)

# Debug: Check environment variables and working directory
print("Current working directory:", os.getcwd())
print(".env file exists:", os.path.exists(".env"))

def sanitize_filename(text: str) -> str:
    """Convert text to a safe filename by removing special characters and replacing spaces."""
    if not text:
        text = "unknown_topic"
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)  # Remove special characters
    text = re.sub(r'\s+', '_', text.strip())  # Replace spaces with underscores
    return text

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Initialize ChatAnthropic
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0)

# Set up the Pydantic parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Define the prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools. 
            Set the 'topic' field to the main subject of the query (e.g., 'Supply Chain' for 'What is supply chain?').
            Wrap the output as a JSON string in triple backticks (```) and provide no other text:
            ```
            {format_instructions}
            ```
            """
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}")
    ]
).partial(format_instructions=parser.get_format_instructions())

# Define tools
tools = [search_tool, wiki_tool, save_tool]

# Create the agent
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

# Create the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Get user input and invoke the agent
query = input("What can I help you research? ")
print(f"User query: {query}")
raw_response = agent_executor.invoke({"query": query})

# Parse the response and save to file
try:
    # Extract the JSON string from the first message's text field
    output_text = raw_response["output"][0]["text"] if isinstance(raw_response["output"], list) and raw_response["output"] else raw_response.get("output")
    print(f"Raw output text: {output_text}")
    structured_response = parser.parse(output_text)
    print(f"Parsed topic: {structured_response.topic}")
    # Format the response as clean plain text
    response_text = (
        f"Topic: {structured_response.topic}\n"
        f"Summary: {structured_response.summary}\n"
        f"Sources:\n" + "\n".join(f"  - {source}" for source in structured_response.sources) + "\n"
        f"Tools Used: {', '.join(structured_response.tools_used)}"
    )
    # Generate a unique filename based on the topic
    topic = structured_response.topic if structured_response.topic.strip() else query
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"research_output_{sanitize_filename(topic)}_{timestamp}.txt"
    print(f"Generated filename: {filename}")
    print(f"Attempting to save to: {os.path.join(os.getcwd(), filename)}")
    # Save the response to the topic-specific file using save_tool
    result = save_tool.run({"data": response_text, "filename": filename})
    print(f"Save result: {result}")
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)
    # Fallback to timestamp-based filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"research_output_error_{timestamp}.txt"
    print(f"Fallback filename: {filename}")
    print(f"Fallback: Attempting to save to: {os.path.join(os.getcwd(), filename)}")
    response_text = f"Error occurred: {str(e)}\nRaw Response: {json.dumps(raw_response, indent=2)}"
    result = save_tool.run({"data": response_text, "filename": filename})
    print(f"Fallback save result: {result}")