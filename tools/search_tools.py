# tools/search_tools.py
from crewai_tools import SerperDevTool

try:
    from crewai_tools import DuckDuckGoSearchTool
    _ddg = DuckDuckGoSearchTool()   # key-free fallback
except Exception:
    _ddg = None

class SearchTools:
    # Primary (needs SERPER_API_KEY)
    search_internet = SerperDevTool()
    # Optional fallback
    search_fallback = _ddg

    @classmethod
    def tools(cls):
        tools = [cls.search_internet]
        if cls.search_fallback is not None:
            tools.append(cls.search_fallback)
        return tools
