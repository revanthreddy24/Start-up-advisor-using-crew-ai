# src/crew.py
from crewai import Crew, Process
from .agents import (
    startup_strategist,
    market_researcher,
    product_designer,
    growth_marketer,
    funding_analyst,
)
from .tasks import (
    idea_refinement_task,
    market_research_task,
    product_spec_task,
    go_to_market_task,
    pitch_outline_task,
)
from .tools import research_tools

def build_startup_crew(user_idea: str) -> Crew:
    strategist = startup_strategist()
    researcher = market_researcher(tools=research_tools())
    prod = product_designer()
    marketer = growth_marketer()
    funder = funding_analyst()

    t1 = idea_refinement_task(strategist, user_idea)
    t2 = market_research_task(researcher, context_tasks=[t1])
    t3 = product_spec_task(prod, context_tasks=[t1, t2])
    t4 = go_to_market_task(marketer, context_tasks=[t1, t2, t3])
    t5 = pitch_outline_task(funder, context_tasks=[t1, t2, t3, t4])

    crew = Crew(
        agents=[strategist, researcher, prod, marketer, funder],
        tasks=[t1, t2, t3, t4, t5],
        process=Process.sequential,  # or Process.hierarchical with manager_llm
        verbose=True,
    )
    return crew
