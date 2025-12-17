# src/tools.py
from crewai_tools import SerperDevTool  # requires SERPER_API_KEY in .env

def research_tools():
    return [SerperDevTool()]
