# Flight Finder and Trip Planner Using CrewAI 

A CrewAI agent based app that helps you in finding flights and planning your itinerary at the destination with top recommended places to visit.


# Required API Keys

1. OpenAI
2. SerpAPI (for Google Flights)
3. Serper API (for web searchs)

Add the above API keys in `.env` file

# How to Run:

Note: _The code is tested on Python version: 3.12.0_

1. Clone the repo
2. `pip install uv`
3. Create virtual environment using, `uv venv --python 3.12`
4. Run `crewai run`

> [!CAUTION]
> Google SERPAPI is used here to search for flights. If using a free tier, it shouldn't be used for commercial purposes.


# Sample Results:

1. The output is stored as a `trip_itinerary.md` file
