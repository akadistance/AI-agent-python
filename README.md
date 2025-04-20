# A.I Agent

A research assistant tool that uses LangChain and Anthropic's Claude to answer user queries, leveraging Wikipedia and DuckDuckGo search. The tool generates a unique text file for each query, named with the topic and timestamp, containing the research summary, sources, and tools used.

**Purpose:** This project is designed for educational use, providing a simple way to research topics and save structured outputs for academic submissions.

## Prerequisites

To run this project, you need the following installed on your system:

- **Python 3.11 or 3.12**: Python 3.13 may have compatibility issues with some dependencies. Python 3.11 is recommended.
- **pip**: Python's package manager, typically included with Python.
- **Git**: Optional, for cloning the repository.
- **Virtual Environment** (Optional but Recommended): To isolate project dependencies.

## Setup Instructions

Follow these steps to set up and run the project on macOS or Windows:

### 1. Clone or Download the Repository

If you have Git installed, clone the repository:
```bash
git clone <repository-url>
cd A.I-Agent
```

Alternatively, download the project files and extract them to a directory, e.g., `~/A.I-Agent/` (macOS) or `C:\A.I-Agent\` (Windows).

### 2. Install Python

Ensure Python 3.11 or 3.12 is installed. To check:

**macOS:**
```bash
python3 --version
```

**Windows:**
```bash
python --version
```

If Python is not installed or you have Python 3.13:

**macOS:**
```bash
brew install python@3.11
```

**Windows:**
Download Python 3.11 from [python.org](https://www.python.org/downloads/). During installation, check "Add Python to PATH".

### 3. Set Up a Virtual Environment

Create a virtual environment to isolate dependencies:

**macOS:**
```bash
python3.11 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

When activated, your terminal prompt should show `(venv)`.

### 4. Install Dependencies

Install the required Python packages using pip:

```bash
pip install langchain langchain-core langchain-community langchain-anthropic pydantic python-dotenv
```

If you have a requirements.txt file:

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root to store your Anthropic API key:

**macOS:**
```bash
touch .env
```
Edit .env using a text editor and add:

```
ANTHROPIC_API_KEY=your-api-key-here
```
**Windows:**
```bash
echo. > .env
```
Edit .env using Notepad or another text editor and add:

```
ANTHROPIC_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual Anthropic API key from Anthropic's website.

Get your API key from:
```
https://console.anthropic.com/settings/keys
```

### 6. Verify Permissions

Ensure the project directory has write permissions to create output files:

**macOS:**
```bash
chmod -R u+rw .
```

**Windows:**
Ensure your user account has write access to the project directory.

## Running the Project

1. **Navigate to the Project Directory:**
    ```bash
    cd path/to/A.I-Agent
    ```

2. **Activate the Virtual Environment** (if not already active):
    ```bash
    source venv/bin/activate  # macOS
    venv\Scripts\activate     # Windows
    ```

3. **Run the Script:**
    ```bash
    python3 main.py
    ```

4. **Enter a Query:**
    When prompted ("What can I help you research?"), enter a topic, e.g., "What is supply chain?" or "Tell me about Apple iPhones."

5. **Check Output:**
    The script generates a unique text file in the project directory, named with the topic and timestamp.

## Example Output

```
--- Research Output ---
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
- **requirements.txt**: Lists Python dependencies for easy installation.

## Troubleshooting

- **Module Not Found:**
  ```bash
  pip install langchain langchain-core langchain-community langchain-anthropic pydantic python-dotenv
  ```

- **API Key Error:** Verify the .env file exists and contains a valid ANTHROPIC_API_KEY.

- **Permission Denied:** Check folder write permissions.

- **Python Version Issues:** If using Python 3.13, switch to Python 3.11.

- **No Output Files:** Check the terminal for errors.

## Notes

- Each query generates a unique file to avoid duplicates or overwriting.
- The project is designed for simplicity, suitable for academic submissions.
