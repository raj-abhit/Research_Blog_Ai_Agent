# Research and Blog AI Agent

An intelligent multi-agent system powered by [crewAI](https://crewai.com) that automatically generates detailed research reports and converts them into engaging blog posts on any topic.

## 🚀 Features

- **Automated Research**: AI agents conduct comprehensive research on any topic
- **Blog Generation**: Automatically converts research into easy-to-read blog posts
- **Multi-Agent Collaboration**: Two specialized agents work together (Research Generator & Blog Writer)
- **LLM Integration**: Supports multiple LLM providers (OpenAI, Groq, Anthropic, etc.)
- **Easy Execution**: Simple batch file for Windows or command-line execution

## 📋 Prerequisites

- Python >=3.10 <3.14
- LLM API Key (Groq, OpenAI, or other supported providers)

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/raj-abhit/Research_Blog_Ai_Agent.git
cd Research_Blog_Ai_Agent
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -e .
```

4. Configure your API key in `.env`:
```env
MODEL=groq/llama-3.1-8b-instant
GROQ_API_KEY=your-api-key-here
```

## 🎯 Usage

### Windows (Easy Way)
Double-click `run.bat` or run:
```cmd
run.bat
```

### Command Line
```bash
python -m research_and_blog_crew.main
```

Or use the installed script:
```bash
run_crew
```

## 📁 Project Structure

```
research_and_blog_crew/
├── src/
│   └── research_and_blog_crew/
│       ├── config/
│       │   ├── agents.yaml      # Agent definitions
│       │   └── tasks.yaml       # Task configurations
│       ├── tools/
│       │   └── custom_tool.py   # Custom tools
│       ├── crew.py              # Main crew logic
│       └── main.py              # Entry point
├── blogs/                       # Generated blog posts
├── knowledge/                   # User preferences
└── run.bat                      # Windows launcher
```

## 🤖 Agents

1. **Report Generator**: Expert researcher that creates detailed, multi-dimensional reports
2. **Blog Writer**: Transforms research into engaging, fun-to-read blog content

## 🛠️ Customization

**Change the topic**: Edit `main.py`
```python
inputs = {
    'topic': 'Your Topic Here',
}
```

**Modify agents**: Edit `config/agents.yaml`
**Modify tasks**: Edit `config/tasks.yaml`

**Add custom tools**: Create new tools in `tools/custom_tool.py`
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
