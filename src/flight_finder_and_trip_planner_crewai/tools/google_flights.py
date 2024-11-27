from crewai.tools import BaseTool
from typing import Any, Optional
from serpapi import GoogleSearch
from dotenv import load_dotenv
from pydantic import BaseModel
import os

# Load environment variables
load_dotenv()


SERPAPI_KEY = os.getenv("SERPAPI_KEY")


class SearchFlightsInput(BaseModel):
    origin: str
    destination: str
    departure_date: str
    return_date: Optional[str] = None


class SearchFlights(BaseTool):
    name: str = "Search Flights Tool"
    description: str = (
        "This tool queries Google Flights SerpAPI, which helps in searching for flights "
        "for a given Origin/Destination combination and specified Departure/Return dates. "
        "The return date is optional."
    )
    args_schema = SearchFlightsInput

    def _run(
        self,
        origin: str,
        destination: str,
        departure_date: str,
        return_date: Optional[str] = None,
    ) -> Any:
        """Run the flight search with provided arguments."""
        if not SERPAPI_KEY:
            raise ValueError("SERPAPI_API_KEY environment variable is not set")

        params = {
            "engine": "google_flights",
            "departure_id": origin,
            "arrival_id": destination,
            "outbound_date": departure_date,
            "return_date": return_date,
            "currency": "USD",
            "hl": "en",
            "api_key": SERPAPI_KEY,
        }

        if return_date:
            params["type"] = "1"  # Round Trip (Default selection)
        else:
            params["type"] = "2"  # One Way

        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            if "error" in results:
                raise ValueError(f"SerpAPI error: {results['error']}")
            return results.get("best_flights")
        except Exception as e:
            raise Exception(f"Failed to search flights: {str(e)}")
