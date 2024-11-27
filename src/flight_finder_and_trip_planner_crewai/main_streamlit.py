import streamlit as st
import warnings
from datetime import datetime
from flight_finder_and_trip_planner_crewai.crew import FlightFinderCrewai

# Suppress specific warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


# Helper function to validate date format
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Streamlit app definition
def main():
    # Configure page layout
    st.set_page_config(
        page_title="Flight Finder and Trip Planner",
        page_icon="✈️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Add title with emoji
    st.markdown(
        """
        <style>
        .main-title {
            text-align: center;
            font-size: 3rem;
            color: #0078D7;
        }
        .description {
            text-align: center;
            color: #6c757d;
            margin-top: -15px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<h1 class="main-title">🌍✈️ Flight Finder and Trip Planner</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="description">Search for the best flights and plan your trips effortlessly!</p>',
        unsafe_allow_html=True,
    )

    # Create layout with columns
    input_col, result_col = st.columns([1, 2])

    # Input fields in the left column
    with input_col:
        st.subheader("Search Inputs")
        origin = st.text_input(
            "Origin (Airport Code)",
            value="HKG",
            help="Enter the 3-letter airport code (e.g., HKG).",
        )
        destination = st.text_input(
            "Destination (Airport Code)",
            value="LAX",
            help="Enter the 3-letter airport code (e.g., LAX).",
        )
        departure_date = st.text_input(
            "Departure Date (YYYY-MM-DD)", value="2024-12-25", help="Format: YYYY-MM-DD"
        )
        return_date = st.text_input(
            "Return Date (optional, YYYY-MM-DD)",
            value="",
            help="Leave empty for one-way trips.",
        )

        # Submit button
        if st.button("🔍 Find Flights"):
            # Validate dates
            if not validate_date(departure_date):
                st.error("Invalid format for Departure Date. Please use YYYY-MM-DD.")
                return
            if return_date and not validate_date(return_date):
                st.error("Invalid format for Return Date. Please use YYYY-MM-DD.")
                return

            inputs = {
                "origin": origin,
                "destination": destination,
                "departure_date": departure_date,
                "return_date": return_date if return_date else None,
            }

            try:
                # st.write("Searching for flights and planning your itinerary...")
                # Run the crew process
                result = FlightFinderCrewai().crew().kickoff(inputs=inputs)

                # Display the result on the right
                with result_col:
                    st.success("Flight search completed successfully!")
                    # st.subheader("Search Results")
                    st.markdown(result, unsafe_allow_html=True)
            except Exception as e:
                with result_col:
                    st.error(f"An error occurred: {str(e)}")

    # Add background styling
    st.markdown(
        """
        <style>
        body {
            background-color: var(--background-color);
            color: var(--text-color);
        }

        .stButton>button {
            background-color: var(--button-background);
            color: var(--button-text-color);
        }

        .stMarkdown {
            color: var(--markdown-text-color);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# Run the app
if __name__ == "__main__":
    main()
