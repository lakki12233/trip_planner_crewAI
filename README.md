# Trip Planner CrewAI (Gemini + Serper) 🧳🗺️

A simple **CrewAI** multi-agent app that:
1) picks the best city for your trip,
2) gathers local insights, and
3) generates a 7-day itinerary.

The plan is saved to **`trip_plan.md`** (and optionally **`trip_plan.pdf`**).

---

## ✨ Features

- Three collaborating agents (city selection, local expert, concierge)
- Web search via **Serper** (+ optional DuckDuckGo fallback if available)
- Website reading/scraping with **crewai-tools**
- Uses **Gemini** models (Google AI Studio REST) through CrewAI’s `LLM`
- Exports to Markdown and (optional) PDF

---

## 🧱 Tech Stack

- **Python** 3.10+
- **CrewAI** (`Agent`, `Task`, `Crew`)
- **crewai-tools** (Serper, Website reader)
- **Gemini API** (Google AI Studio REST)
- **python-dotenv** (env management)
- **ReportLab** *(optional, for PDF export)*

**Key Files**
trip_planner_crewAI/
├─ main.py # Entry point; prompts user & runs crew; writes trip_plan.md (+ optional PDF)
├─ trip_agents.py # Agent definitions + shared LLM config (Gemini default)
├─ trip_tasks.py # Task prompts and expected outputs
├─ tools/
│ ├─ init.py
│ ├─ search_tools.py # Serper primary + optional DuckDuckGo fallback
│ ├─ browser_tools.py # Website reader (compat shim across crewai-tools versions)
│ └─ export_pdf.py # Tiny Markdown -> PDF helper (optional)
├─ requirements.txt # (Optional) Pinned deps
├─ .env # (User-provided) API keys & config
└─ README.md


---

## 📦 Requirements

- Python **3.10** or newer
- **Serper** API key → https://serper.dev/
- **Gemini** API key (Google AI Studio REST) → https://ai.google.dev/

> You **do not** need OpenAI keys for this setup.

---

## ⚡ Quick Start

> Commands shown for **Windows PowerShell**. macOS/Linux equivalents included.

### 1) Clone
```powershell
git clone https://github.com/lakki12233/trip_planner_crewAI.git
cd trip_planner_crewAI
