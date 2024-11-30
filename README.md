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
4. Run `crewai install` to install all the dependencies
5. Run `crewai run`

> [!CAUTION]
> Google SERPAPI is used here to search for flights. If using a free tier, it shouldn't be used for commercial purposes.

# Streamlit App:

If you want to run this as a Streamlit app follow the steps:

1. Clone the repo
2. Install UV: `pip install uv`
3. Create virtual environment using, `uv venv --python 3.12`
4. Install the libraries mentioned in `pyproject.toml` dependencies section using `uv pip install xxxxxx`
5. To run the app: `streamlit run main_streamlit.py` and follow the instructions to access it in a browser

# Sample Results:

## CrewAI Run: 
The output is stored as a `trip_itinerary.md` file:

<img width="964" alt="Screenshot 2024-11-25 at 9 46 17 PM" src="https://github.com/user-attachments/assets/98c1ea7c-96b6-453d-8292-c05e05d6dd24">
<img width="964" alt="Screenshot 2024-11-25 at 9 46 44 PM" src="https://github.com/user-attachments/assets/9b4c241d-e750-4000-86ad-53d8ff033938">


## Output of Streamlit app:
<img width="1440" alt="Screenshot 2024-11-26 at 8 53 52 PM" src="https://github.com/user-attachments/assets/9ab5a7af-9457-4da4-a669-3680995b6dd4">
<img width="1440" alt="Screenshot 2024-11-26 at 8 54 15 PM" src="https://github.com/user-attachments/assets/9c0a8602-1b66-4534-9ed3-884229f5267b">
<img width="1440" alt="Screenshot 2024-11-26 at 8 54 24 PM" src="https://github.com/user-attachments/assets/65d7d002-3361-4b0b-be52-c3e0c1d239d4">
