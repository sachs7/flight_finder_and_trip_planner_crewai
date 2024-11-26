from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# Custom Tool
from flight_finder_and_trip_planner_crewai.tools.google_flights import SearchFlights
import os

model = LLM(model=os.environ.get("MODEL"), api_key=os.environ.get("OPENAI_API_KEY"))


@CrewBase
class FlightFinderCrewai:
    """FlightFinderCrewai crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def travel_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["travel_agent"],
            tools=[
                SearchFlights(),
            ],  # Example of custom tool, loaded on the beginning of file
            verbose=True,
            llm=model,
        )

    @agent
    def tour_planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["tour_planner_agent"],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
            ],
            verbose=True,
            llm=model,
        )

    @agent
    def summary_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["summary_agent"], verbose=True, llm=model
        )

    @task
    def travel_agent_task(self) -> Task:
        """Task for finding flights."""
        return Task(config=self.tasks_config["travel_agent_task"])

    @task
    def tour_planner_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config["tour_planner_agent_task"],
        )

    @task
    def summary_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config["summary_agent_task"],
            output_file="trip_itinerary.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FlightFinderCrewai crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
