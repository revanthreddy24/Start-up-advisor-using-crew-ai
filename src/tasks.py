# src/tasks.py
from crewai import Task

def idea_refinement_task(agent, user_idea: str):
    return Task(
        description=f"""
        Take this raw startup idea: '{user_idea}'.

        1. Clarify the core problem and who experiences it.
        2. Propose at least 2-3 differentiated angles / unique value propositions.
        3. Highlight main risks and key assumptions to validate.

        Focus on being clear, concise, and practical for a technical founder.
        """,
        expected_output=(
            "A short brief with sections: Problem, Target User, "
            "Solution Overview, Differentiation, Key Risks & Assumptions."
        ),
        agent=agent,
    )

def market_research_task(agent, context_tasks):
    return Task(
        description="""
        Using the refined idea and context from previous tasks, perform lean market research:
        1. Estimate market size (TAM/SAM/SOM qualitatively is fine).
        2. Identify 3-7 key competitors or closest alternatives.
        3. Summarize how this startup could position itself relative to them.
        """,
        expected_output=(
            "A short market note with bullet points for market size, competitor list, "
            "and positioning suggestions."
        ),
        agent=agent,
        context=context_tasks,  # use output of idea refinement
    )

def product_spec_task(agent, context_tasks):
    return Task(
        description="""
        Based on the refined idea and market insights, propose an MVP product spec:
        1. Target user story / main jobs-to-be-done.
        2. Core v1 features (must-have).
        3. Nice-to-have / v2 ideas.
        4. Rough technical stack suggestions (high level).
        """,
        expected_output="A concise MVP spec with clear feature bullets and a short tech notes section.",
        agent=agent,
        context=context_tasks,
    )

def go_to_market_task(agent, context_tasks):
    return Task(
        description="""
        Create a go-to-market brief:
        1. Define ICP(s) and key personas.
        2. Main value prop and 2-3 supporting benefits.
        3. Landing page structure + headline, subheadline, CTA suggestions.
        4. First 2-3 acquisition channels with concrete first experiments.
        """,
        expected_output="A GTM brief and sample landing page copy.",
        agent=agent,
        context=context_tasks,
    )

def pitch_outline_task(agent, context_tasks):
    return Task(
        description="""
        Draft a short investor memo / pitch outline covering:
        1. Problem & solution.
        2. Market & competition (brief).
        3. Product & roadmap.
        4. GTM strategy.
        5. Basic business model and key metrics to track.
        """,
        expected_output="A structured outline suitable to turn into a 10-slide deck.",
        agent=agent,
        context=context_tasks,
        markdown=True,
        output_file="startup_pitch_outline.md",
    )
