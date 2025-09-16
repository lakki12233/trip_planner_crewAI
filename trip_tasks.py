# trip_tasks.py
from crewai import Task
from textwrap import dedent

class TripTasks:
    def __tool_rules(self) -> str:
        # IMPORTANT: Name + exact arg name/type must match tool definitions.
        return dedent("""
        ---
        AVAILABLE TOOLS (use exactly these names):
        1) Search the internet with Serper
           - Action Input (JSON): {"search_query": "<plain string query>"}
           - Examples:
             Action: Search the internet with Serper
             Action Input: {"search_query": "best food cities in India"}

        2) Read website content
           - Action Input (JSON): {"website_url": "<https://...>"}
           - Examples:
             Action: Read website content
             Action Input: {"website_url": "https://example.com/page"}

        RULES:
        - Do NOT invent actions like "Ask the user for ..." or "No action needed".
        - Pass a PLAIN STRING to search_query and a single URL STRING to website_url.
        - Perform at most 2–3 searches per task. If a search fails (429/quota), try a simpler query.
        - After using a tool, continue with Thought → next Action OR produce Final Answer.
        - In the Final Answer, cite the URLs you used.
        ---
        """)

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100!"

    def identify_task(self, agent, origin, cities, interests, range):
        return Task(
            description=dedent(f"""
                Analyze and select the best city for the trip based 
                on weather, seasonality, and travel costs. Compare multiple
                cities on current weather, upcoming events, and overall expenses.

                Your final answer must be a detailed report on the chosen city,
                including actual flight costs, weather forecast, and attractions.

                {self.__tool_rules()}
                {self.__tip_section()}

                Traveling from: {origin}
                City Options: {cities}
                Trip Date: {range}
                Traveler Interests: {interests}
            """),
            agent=agent,
            expected_output="Detailed report on the chosen city including flight costs, weather forecast, and attractions"
        )

    def gather_task(self, agent, origin, interests, range):
        return Task(
            description=dedent(f"""
                Compile an in-depth city guide for an amazing trip: key attractions,
                local customs, special events, hidden gems, weather outlook, and high-level costs.

                {self.__tool_rules()}
                {self.__tip_section()}

                Trip Date: {range}
                Traveling from: {origin}
                Traveler Interests: {interests}
            """),
            agent=agent,
            expected_output="Comprehensive city guide including hidden gems, cultural hotspots, and practical travel tips"
        )

    def plan_task(self, agent, origin, interests, range):
        return Task(
            description=dedent(f"""
                Expand the guide into a complete 7-day itinerary with daily plans,
                real restaurants/hotels/places, weather notes, packing suggestions,
                and a budget breakdown. Be specific and justify picks.

                {self.__tool_rules()}
                {self.__tip_section()}

                Trip Date: {range}
                Traveling from: {origin}
                Traveler Interests: {interests}
            """),
            agent=agent,
            expected_output="Complete expanded travel plan with daily schedule, weather conditions, packing suggestions, and budget breakdown"
        )
