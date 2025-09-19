# CLI AI Agent (Gemini + Tool Calling)

A simple command‑line AI agent powered by Google's Gemini that can plan and call tools to work inside a sandboxed project directory. The agent can list files, read files (with safe truncation), run Python scripts, and write files. A small calculator app is included as a demo workspace the agent can operate on.

## Installation

- **Requirements**: Python >= 3.12
- **Dependencies**: Managed via `pyproject.toml`

Option A — Using uv (recommended)

```bash
uv sync
source .venv/bin/activate
```

Option B — Using pip

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install google-genai==1.12.1 python-dotenv==1.1.0
```

Set your Gemini API key (create a `.env` file or export directly):

```bash
echo 'GEMINI_API_KEY=your_api_key_here' > .env
# or: export GEMINI_API_KEY=your_api_key_here
```

## Quick Start

Run the agent with a natural‑language prompt:

```bash
uv run main.py "List the files in the working directory and show me the calculator entry point" --verbose
```

- The agent executes in an iterative loop (max iterations set by `MAX_ITERS`).
- Tools are constrained to the configured working directory to keep operations safe.

## Usage Examples

- Ask it to inspect the demo calculator project:

```bash
uv run main.py "Scan the current directory, open calculator/main.py, and summarize how it parses expressions."
```

- Run the calculator app via the agent tools:

```bash
uv run main.py "Execute calculator/main.py with the argument '3 + 5' and show me the program output."
```

- Create or modify a file safely within the working directory:

```bash
uv run main.py "Write a new file calculator/README.md with a short description of the calculator. Then list files again."
```

- Read a specific file with truncation protection:

```bash
uv run main.py "Read calculator/pkg/calculator.py and extract the supported operators and precedence."
```

## Features

- **AI Agent with Tool Calling**: Uses Google Gemini to plan and execute multi-step tasks
- **File Operations**: List, read, and write files safely within a sandboxed directory
- **Python Execution**: Run Python scripts with arguments and capture output
- **Safety Controls**: Path restrictions, file size limits, execution timeouts
- **Configurable**: Adjust working directory, max iterations, and file read limits
- **Verbose Mode**: See token usage and tool call details

## Environment

- Model: `gemini-2.0-flash-001`
- API: `google-genai`
- Env var: `GEMINI_API_KEY`

## Notes

- The agent loops until it returns a final text response or hits `MAX_ITERS`.
- Tool responses are fed back to the model to enable multi‑step plans.
- Errors from tools are returned as readable messages for transparency.


