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

---

## 📂 Project Structure

```text
trip_planner_crewAI/
├─ main.py             # Entry point; prompts user & runs crew; writes trip_plan.md (+ optional PDF)
├─ trip_agents.py      # Agent definitions + shared LLM config (Gemini default)
├─ trip_tasks.py       # Task prompts and expected outputs
├─ tools/
│  ├─ __init__.py
│  ├─ search_tools.py  # Serper primary + optional DuckDuckGo fallback
│  ├─ browser_tools.py # Website reader (compat shim across crewai-tools versions)
│  └─ export_pdf.py    # Tiny Markdown -> PDF helper (optional)
├─ requirements.txt    # (Optional) pinned deps
├─ .env                # (User-provided) API keys & config
└─ README.md
```

---

## 📦 Requirements

- **Python 3.10** or newer  
- **Serper** API key → <https://serper.dev/>  
- **Gemini** API key (Google AI Studio REST) → <https://ai.google.dev/>  

> You **do not** need OpenAI keys for this setup.

---

## ⚡ Quick Start

> Commands shown for **Windows PowerShell** first; **macOS / Linux** alternatives included.

### 1) Clone

#### Windows (PowerShell)
```powershell
git clone https://github.com/lakki12233/trip_planner_crewAI.git
cd trip_planner_crewAI
```

#### macOS / Linux
```bash
git clone https://github.com/lakki12233/trip_planner_crewAI.git
cd trip_planner_crewAI
```

### 2) Create & activate a virtualenv

#### Windows (PowerShell)
```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

#### If `requirements.txt` exists
```bash
pip install -U pip
pip install -r requirements.txt
```

#### If not
```bash
pip install -U pip
pip install crewai crewai-tools python-dotenv
# Optional for PDF export:
pip install reportlab
```

### 4) Configure environment

Create a **`.env`** file in the project root:

```dotenv
# LLM (Gemini via Google AI Studio REST)
GEMINI_API_KEY=YOUR_GEMINI_KEY

# Web search (Serper)
SERPER_API_KEY=YOUR_SERPER_KEY

# Default model (change if desired)
LLM_MODEL=gemini/gemini-1.5-flash-8b
```



### 5) Run

```bash
python main.py
```

You’ll be prompted for **origin**, **candidate cities**, **date range**, and **interests**.  
On success:
- **`trip_plan.md`** is saved
- **`trip_plan.pdf`** is created *if* `reportlab` is installed

---

## 🧠 Model & Tools

**Default model:** `gemini/gemini-2.5-flash-lite` (set via `LLM_MODEL`)  
Other options:
- `gemini/gemini-1.5-flash` *(fast, multimodal)*
- `gemini/gemini-1.5-pro` *(stronger, stricter quotas)*

**Search:** **Serper** (needs `SERPER_API_KEY`). If your `crewai-tools` exposes DuckDuckGo, it’s used as a key-free fallback.

**Website reading:** `tools/browser_tools.py` includes a compatibility shim for different `crewai-tools` versions.

---

## 📄 Output

- **Chosen destination** with reasoning (weather/season/prices)  
- **Local guide** (attractions, customs, hidden gems, costs)  
- **7-day itinerary** (hotels, restaurants, activities)  
- **Packing suggestions** & **budget breakdown**

Saved as:
- `trip_plan.md`
- `trip_plan.pdf` *(if ReportLab installed)*

---

## 🔧 Configuration Reference

| Variable         | Required | Example                      | Notes                                              |
|------------------|:--------:|------------------------------|----------------------------------------------------|
| `GEMINI_API_KEY` |   Yes    | `ya29...`                    | Google AI Studio REST API key                      |
| `SERPER_API_KEY` |   Yes*   | `SERP-xxxxxxxx`              | Needed unless DuckDuckGo fallback is available     |
| `LLM_MODEL`      |    No    | `gemini/gemini-2.5-flash-lite` | Swap to `-flash` or `-pro` as desired              |

\* If `crewai-tools` includes DuckDuckGo, the app will attempt a **fallback** when Serper is unavailable.

---

## 🩺 Troubleshooting

**`ImportError: WebsiteReadTool not found`**  
```bash
pip install -U crewai-tools
```
*(Our `browser_tools.py` already tries alternative class names across versions.)*

**Serper validation/quota errors**  
- Check `SERPER_API_KEY` in `.env`.  
- If quota is exceeded, agents may output placeholders.  
- Use DuckDuckGo fallback (if available) or wait for reset.

**Gemini `429 / RESOURCE_EXHAUSTED`**  
- Change `LLM_MODEL` (e.g., `gemini/gemini-2.5-flash-lite`)  
- Add billing / increase quota  
- Re-run after reset

**“Invalid response from LLM call – None or empty”**  
- Usually transient. Re-run or switch models.

---

## 🛠️ Customization

- Edit **`trip_tasks.py`** to tweak prompts & outputs.  
- Adjust **`trip_agents.py`** to change tools/roles/LLM params.  
- Modify search behavior in **`tools/search_tools.py`**.  
- Tweak PDF formatting in **`tools/export_pdf.py`**.

---

## 🔐 Privacy

- Keep secrets in `.env` 
- Generated content may include public web data—review before sharing.

---

## 🙌 Credits

Built with **CrewAI**, **crewai-tools**, and **Gemini (Google AI Studio)**. ✈️
