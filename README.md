# PythonAIAgentClaude

A research assistant tool that uses LangChain and Anthropic's Claude to answer user queries, leveraging Wikipedia and DuckDuckGo search. The tool generates a unique text file for each query, named with the topic and timestamp, containing the research summary, sources, and tools used.

**Developed by:** Jason Jiwan 
**Purpose:** This project is designed for educational use, providing a simple way to research topics and save structured outputs for academic submissions.

## Prerequisites

To run this project, you need the following installed on your system:

- **Python 3.11 or 3.12**: Python 3.13 may have compatibility issues with some dependencies. Python 3.11 is recommended.
- **pip**: Python's package manager, typically included with Python.
- **Git**: Optional, for cloning the repository.
- **Virtual Environment**: Optional but recommended to isolate project dependencies.

## Setup Instructions

Follow these steps to set up and run the project on macOS or Windows:

### 1. Clone or Download the Repository

If you have Git installed, clone the repository:
```
git clone <repository-url>
cd A.I-Agent
```

Alternatively, download the project files and extract them to a directory, e.g., `~/A.I-Agent/` (macOS) or `C:\A.I-Agent\` (Windows).

### 2. Install Python

Ensure Python 3.11 or 3.12 is installed. To check:

**macOS:**
```
python3 --version
```

**Windows:**
```
python --version
```

If Python is not installed or you have Python 3.13:

**macOS:**
```
brew install python@3.11
```

**Windows:** Download Python 3.11 from python.org. During installation, check "Add Python to PATH".

For other platforms, download from python.org.

### 3. Set Up a Virtual Environment

Create a virtual environment to isolate dependencies:

**macOS:**
```
python3.11 -m venv venv
source venv/bin/activate
```

**Windows:**
```
python -m venv venv
venv\Scripts\activate
```

When activated, your terminal prompt should show (venv).

### 4. Install Dependencies

Install the required Python packages using pip:

**macOS/Windows:**
```
pip install langchain langchain-core langchain-community langchain-anthropic pydantic python-dotenv
```

If you have a requirements.txt file:
```
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a .env file in the project root to store your Anthropic API key:

**macOS:**
```
touch .env
```
Edit .env using a text editor (e.g., nano .env) and add:
```
ANTHROPIC_API_KEY=your-api-key-here
```

**Windows:**
```
echo. > .env
```
Edit .env using Notepad or another text editor and add:
```
ANTHROPIC_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual Anthropic API key from Anthropic's website.

### 6. Verify Permissions

Ensure the project directory has write permissions to create output files:

**macOS:**
```
chmod -R u+rw .
```

**Windows:** Ensure your user account has write access to the project directory. Right-click the A.I-Agent folder, select "Properties" > "Security," and confirm your user has "Full control."

## Running the Project

1. **Navigate to the Project Directory:**

    **macOS:**
    ```
    cd ~/A.I-Agent
    ```

    **Windows:**
    ```
    cd C:\A.I-Agent
    ```

2. **Activate the Virtual Environment** (if not already active):

    **macOS:**
    ```
    source venv/bin/activate
    ```

    **Windows:**
    ```
    venv\Scripts\activate
    ```

3. **Run the Script:**

    **macOS:**
    ```
    python3 main.py
    ```

    **Windows:**
    ```
    python main.py
    ```

4. **Enter a Query:** When prompted (What can I help you research?), enter a topic, e.g., "What is supply chain?" or "Tell me about Apple iPhones."

5. **Check Output:**

    The script generates a unique text file in the project directory, named with the topic and timestamp.

    To view the file:

    **macOS:**
    ```
    cat research_output_*.txt
    ```

    **Windows:**
    ```
    type research_output_*.txt
    ```

### Example Output:
```
--- Research Output ---
Developed by: Jason Jiwan
Timestamp: 2025-04-19 16:12:00

Topic: Supply Chain
Summary: A supply chain is a complex network of organizations, people, activities, information, and resources involved in delivering a product or service from supplier to end user...
Sources:
  - Wikipedia - Supply Chain
  - Various online business and logistics resources...
Tools Used: wikipedia, search
```

## Project Structure

- **main.py**: The main script that runs the research assistant, processes queries, and saves outputs.
- **tools.py**: Defines tools for searching (DuckDuckGo), querying Wikipedia, and saving results to text files.
- **.env**: Stores the Anthropic API key (not included in the repository).
- **research_output_*.txt**: Output files generated for each query.
- **README.md**: This file, providing setup and usage instructions.

## Troubleshooting

- **Module Not Found:** Ensure all dependencies are installed:
  ```
  pip install langchain langchain-core langchain-community langchain-anthropic pydantic python-dotenv
  ```

- **API Key Error:** Verify the .env file exists and contains a valid ANTHROPIC_API_KEY.

- **Permission Denied:**
  
  **macOS:**
  ```
  chmod -R u+rw .
  ```
  
  **Windows:** Check folder permissions in "Properties" > "Security."

- **Python Version Issues:** If using Python 3.13, switch to Python 3.11:
  
  **macOS:**
  ```
  brew install python@3.11
  /usr/local/bin/python3.11 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
  
  **Windows:**
  ```
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

- **No Output Files:** Check the terminal for errors, especially "save_to_txt received filename". Share the output for debugging.

## Notes

- Each query generates a unique file to avoid duplicates or overwriting, using a topic and timestamp format.
- The project is designed for simplicity, suitable for academic submissions.
- For additional help, contact the developer or check the repository's issue tracker.
