import logging
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

load_dotenv()

logging.basicConfig(level=logging.INFO)

console = Console()

try:
    search_agent = Agent(
        name="Web Search Agent",
        description="Agent for searching AI-related queries",
        model=Groq(id="mixtral-8x7b-32768"),
        instructions="Provide AI-related search responses concisely.",
        show_tool_calls=False,
        markdown=True,
        debug_mode=True
    )

    query = "What are the latest AI developments in 2025?"
    console.print(Panel(f"[bold green]Query:[/bold green] {query}", title="🔍 Search Query", expand=False))

    response = search_agent.run(message=query)

    console.print(Panel(f"[bold cyan]{response}[/bold cyan]", title="🌍 AI Response", expand=False))

except Exception as e:
    logging.error(f"Error running the search agent: {str(e)}")
