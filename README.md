FILE 3: README.md
=========================================
# Cursor AI Automated Code Reviewer

A local Python automation tool that scans project directories for source code files, connects to free-tier LLM endpoints via OpenRouter, and generates a structured markdown code review report.

## Features
* **Directory Scanning:** Automatically detects code files (`.py`, `.java`, `.cpp`) in your local workspace.
* **AI-Powered Code Analysis:** Sends source code to free-tier LLM endpoints for bug detection, efficiency improvements, and best practices.
* **Automated Documentation:** Compiles all feedback into a clean, unified `REVIEW.md` report.

## Tech Stack
* Python
* OpenAI Python SDK (routed via OpenRouter)
* Markdown

## How to Run

1. Clone the repository:
   git clone https://github.com/Afk2598/cursor-code-reviewer.git

2. Install the required dependency:
   pip install -r requirements.txt

3. Place any code files you want reviewed into the folder and execute:
   python code_reviewer.py
