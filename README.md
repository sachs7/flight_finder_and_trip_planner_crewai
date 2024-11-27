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
2. Install UV: `pip install uv`
3. Create virtual environment using, `uv venv --python 3.12`
4. Run `crewai run`

> [!CAUTION]
> Google SERPAPI is used here to search for flights. If using a free tier, it shouldn't be used for commercial purposes.

# Streamlit App:

If you want to run this as a Streamlit app follow the steps:

1. Clone the repo
2. Install UV: `pip install uv`
3. Create virtual environment using, `uv venv --python 3.12`
4. Install the libraries mentioned in `pyproject.toml` dependencies section (OR if you have `poetry` available, then do: `poetry install`)
5. To run the app: `streamlit run main_streamlit.py` and follow the instructions to access it in a browser

# Sample Results:

1. The output is stored as a `trip_itinerary.md` file:

<img width="964" alt="Screenshot 2024-11-25 at 9 46 17 PM" src="https://github.com/user-attachments/assets/98c1ea7c-96b6-453d-8292-c05e05d6dd24">
<img width="964" alt="Screenshot 2024-11-25 at 9 46 44 PM" src="https://github.com/user-attachments/assets/9b4c241d-e750-4000-86ad-53d8ff033938">


2. Output of Streamlit app: