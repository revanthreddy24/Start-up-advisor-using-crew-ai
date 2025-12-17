# src/run.py
import os
from dotenv import load_dotenv
from .crew import build_startup_crew

def run_startup_agent():
    load_dotenv()
    idea = input("Describe your startup idea (or problem) in 2-5 sentences:\n> ")
    crew = build_startup_crew(idea)
    result = crew.kickoff()
    print("\n=== FINAL RESULT ===\n")
    print(result)  # pitch_outline_task has markdown + file output

if __name__ == "__main__":
    run_startup_agent()
