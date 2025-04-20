from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import StructuredTool
from langchain.tools import Tool
from pydantic import BaseModel
from datetime import datetime

class SaveToolArgs(BaseModel):
    data: str
    filename: str

def save_to_txt(data: str, filename: str) -> str:
    """Saves the provided data to a text file with the specified filename."""
    try:
        print(f"save_to_txt received data: {data[:100]}...")  # Truncate for brevity
        print(f"save_to_txt received filename: {filename}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_text = (
            f"--- Research Output ---\n"
            f"Timestamp: {timestamp}\n\n"
            f"{data}\n\n"
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(formatted_text)
        print(f"File written successfully to {filename}")
        return f"Data successfully saved to {filename}"
    except Exception as e:
        error_msg = f"Error writing to {filename}: {str(e)}"
        print(error_msg)
        return error_msg

save_tool = StructuredTool.from_function(
    func=save_to_txt,
    name="save_text_to_file",
    description="Saves structured research data to a text file. Requires 'data' (the content to save) and 'filename' (the name of the file).",
    args_schema=SaveToolArgs
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information"
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)