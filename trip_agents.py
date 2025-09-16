# trip_agents.py
import os
from dotenv import load_dotenv
load_dotenv(".env", override=True)

from crewai import Agent, LLM
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools

# --- LLM: Gemini 2.5 Flash-Lite (good free-tier limits) ---
llm = LLM(
    model=os.getenv("LLM_MODEL", "gemini/gemini-2.5-flash-lite"),
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.4,
    max_retries=2,  # don't burn quota on repeated retries
    litellm_params={
        "api_base": "https://generativelanguage.googleapis.com",  # Gemini REST (not Vertex)
        "timeout": 90,
        "max_tokens": 900,  # keeps responses concise and cheaper
    },
)

# (optional but recommended) one-line tools list to reuse across agents
TOOLS = SearchTools.tools() + [BrowserTools.scrape]


class TripAgents:
    def city_selection_agent(self) -> Agent:
        return Agent(
            role="City Selection Expert",
            goal="Select the best city based on weather, season, and prices.",
            backstory="Expert in analyzing travel data to pick ideal destinations.",
            tools=TOOLS,
            llm=llm,
            verbose=True,
            allow_delegation=False,
            max_iter=3,
        )

    def local_expert(self) -> Agent:
        return Agent(
            role="Local City Expert",
            goal="Provide the BEST insights about the selected city.",
            backstory="Knowledgeable local guide with deep info on attractions and customs.",
            tools=TOOLS,
            llm=llm,
            verbose=True,
            allow_delegation=False,
            max_iter=3,
        )

    def travel_concierge(self) -> Agent:
        return Agent(
            role="Amazing Travel Concierge",
            goal="Create an amazing itinerary with budget & packing suggestions.",
            backstory="Specialist in travel planning with decades of experience.",
            tools=TOOLS,
            llm=llm,
            verbose=True,
            allow_delegation=False,
            max_iter=3,
        )
