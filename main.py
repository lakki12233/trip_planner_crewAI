# main.py
from crewai import Crew
from textwrap import dedent
from trip_agents import TripAgents
from trip_tasks import TripTasks

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

class TripCrew:
    def __init__(self, origin: str, cities: str, date_range: str, interests: str):
        self.cities = cities
        self.origin = origin
        self.interests = interests
        self.date_range = date_range

    def run(self):
        agents = TripAgents()
        tasks = TripTasks()

        city_selector_agent = agents.city_selection_agent()
        local_expert_agent = agents.local_expert()
        travel_concierge_agent = agents.travel_concierge()

        identify_task = tasks.identify_task(
            city_selector_agent,
            self.origin,
            self.cities,
            self.interests,
            self.date_range,
        )
        gather_task = tasks.gather_task(
            local_expert_agent,
            self.origin,
            self.interests,
            self.date_range,
        )
        plan_task = tasks.plan_task(
            travel_concierge_agent,
            self.origin,
            self.interests,
            self.date_range,
        )

        crew = Crew(
            agents=[city_selector_agent, local_expert_agent, travel_concierge_agent],
            tasks=[identify_task, gather_task, plan_task],
            verbose=True,
        )
        return crew.kickoff()

if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print("-------------------------------")
    location = input(dedent("""\
        From where will you be traveling from?
    """))
    cities = input(dedent("""\
        What are the cities options you are interested in visiting?
    """))
    date_range = input(dedent("""\
        What is the date range you are interested in traveling?
    """))
    interests = input(dedent("""\
        What are some of your high level interests and hobbies?
    """))

    trip_crew = TripCrew(location, cities, date_range, interests)
    result = trip_crew.run()

    # Save Markdown once
    md_path = "trip_plan.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(str(result))
    print("\nSaved Markdown to:", md_path)

    # Export to PDF (optional)
    try:
        from export_pdf import md_to_pdf
        pdf_path = "trip_plan.pdf"
        if md_to_pdf(md_path, pdf_path):
            print("Saved PDF to:", pdf_path)
        else:
            print("PDF export skipped.")
    except ImportError:
        print("PDF export unavailable. Install reportlab: pip install reportlab")

    print("\n\n########################")
    print("## Here is your Trip Plan")
    print("########################\n")
    print(result)
