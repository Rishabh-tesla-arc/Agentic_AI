# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.tools.duckduckgo import DuckDuckGo
# from phi.tools.yfinance import YFinanceTools
# import groq
# import time
# from dotenv import load_dotenv

# load_dotenv()

# web_search_agent = Agent(
#     name="Web Agent",
#     description="This is the agent for searching content from the web",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[DuckDuckGo()],
#     instructions="Always include the sources",
#     show_tool_calls=True,
#     markdown=True,
#     debug_mode=True
# )

# finance_agent = Agent(
#     name="Finance Agent",
#     description="Your task is to find finance information",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[
#         YFinanceTools(
#             stock_price=True,
#             analyst_recommendations=True,
#             company_info=True,
#             company_news=True
#         )
#     ],
#     instructions=["Use tables to display data"],
#     show_tool_calls=True,
#     markdown=True,
#     debug_mode=True
# )

# agent_team = Agent(
#     team=[web_search_agent, finance_agent],
#     model=Groq(id="llama-3.3-70b-versatile"),
#     instructions=["Always include sources", "Use tables to display data"],
#     show_tool_calls=True,
#     markdown=True,
#     debug_mode=True
# )

# def rate_limited_response(agent, query):
#     try:
#         return agent.print_response(query, stream=True)
#     except groq.APIStatusError as e:
#         if "rate_limit_exceeded" in str(e):
#             time.sleep(60)  # Wait 1 minute
#             return agent.print_response(query, stream=True)
#         raise e

# # Use the multi-agent system
# rate_limited_response(
#     agent_team,
#     "Summarize analyst recommendations and share the latest news for TSLA"
# )











import logging
import time
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

load_dotenv()

logging.basicConfig(level=logging.INFO)

console = Console()

finance_agent = Agent(
    name="Finance Agent",
    description="Retrieves financial data",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        )
    ],
    instructions=["Use tables to display data"],
    show_tool_calls=False,
    debug_mode=False
)

multi_agent = Agent(
    team=[finance_agent],
    model=Groq(id="mixtral-8x7b-32768"),
    instructions=["Ensure sources are included", "Use tables where possible"],
    show_tool_calls=False
)

def safe_run(agent, query):
    try:
        return agent.run(message=query)
    except Exception as e:
        logging.warning(f"Rate limit exceeded. Retrying in 60 seconds... {str(e)}")
        time.sleep(60)
        return agent.run(message=query)

query = "Summarize the latest AI trends and Tesla's financial status."
console.print(Panel(f"[bold yellow]Query:[/bold yellow] {query}", title="🚀 Multi-Agent Query", expand=False))

response = safe_run(multi_agent, query)

console.print(Panel(f"[bold cyan]{response}[/bold cyan]", title="📊 Multi-Agent Response", expand=False))
