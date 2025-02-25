<h1 align="center" id="title">Agentic AI</h1>

<p align="center"><img src="https://socialify.git.ci/Rishabh-tesla-arc/Agentic_AI/image?forks=1&amp;issues=1&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Solid&amp;pulls=1&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>

<p id="description">AgenticAI is an AI-powered system that leverages Phidata Groq models and various AI tools to automate web search financial analysis and image recognition. It integrates multiple agents to perform specialized tasks efficiently making it a robust solution for AI-driven applications.<br>
  
The system includes: <br>
* AI-powered web search for retrieving relevant information <br>
* Financial analysis tools for real-time stock data and market insights <br>
* Multi-agent collaboration for handling complex AI workflows <br>
* Image analysis capabilities using Groq models <br>
* API integration for seamless interaction with external data sources</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   AI Project Management: Uses uv for easy environment setup and dependency management
*   Web Search Agent: Retrieves information using DuckDuckGo API
*   Finance Agent: Fetches stock data analyst recommendations and financial news using Yahoo Finance tools
*   Multi-Agent System: Enables agents to work together for advanced AI tasks
*   Image Analysis Agent: Extracts insights from images using Groq models
*   Custom API Integrations: Securely connects to Phidata and Groq Cloud APIs
*   Structured Data Output: Supports markdown tables and formatted responses
*   Rate-Limiting Handling: Implements error handling to manage API request limits
*   Easy Deployment: Compatible with VS Code and command-line execution

<h2>🛠️ Installation Steps:</h2>

<p>1. 1. Open PowerShell as Administrator.</p>

<p>2. Navigate to the desired folder:</p>

```
cd <desired-folder-path>
```

<p>3. Install uv for Python project management:</p>

```
Invoke-WebRequest -Uri https://astral.sh/uv/install.ps1 -OutFile install.ps1;
powershell -ExecutionPolicy Bypass -File ./install.ps1
```

<p>4. Install Python:</p>

```
uv python install 3.12
uv python --version
```

<p>5. Initialize the project:</p>

```
uv init -p 3.12 --name
code .
```

<p>6. Install dependencies:</p>

```
uv add phidata duckduckgo-search groq yfinance
```

<p>7. Set up API keys in .env:</p>

```
PHI_API_KEY="your-phidata-api-key"
GROQ_API_KEY="your-groq-api-key"
```

<p>8. Run AI agents:</p>

```
uv run search_agent.py
uv run finance_agent.py
uv run multi_agent.py
uv run image_agent.py
```

<p>9. Done</p>

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python - Core programming language
*   Phidata - AI framework for intelligent agent development
*   Groq AI Models - Powers natural language and image processing tasks
*   DuckDuckGo Search API - Retrieves web-based information
*   ahoo Finance API - Provides real-time stock market data
*   uv - Environment and dependency management
