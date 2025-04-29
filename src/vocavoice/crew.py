# Import necessary modules from CrewAI
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool

# Import custom TTS tool
from vocavoice.tools.tts_tool import TTSTool

# Initialize tools
file_writer_tool = FileWriterTool()
tts_tool = TTSTool()

@CrewBase
class Vocavoice():
    """ Vocavoice crew """

    # Define paths for agents and tasks configurations
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
            
    # Define TTS Agent
    @agent
    def tts_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["tts_agent"],
            verbose=True,
            tools=[tts_tool],  # Assign TTS tool to the agent
            max_iter=1,        # Agent will execute only once
        )
        
    # Define Script Writer Agent
    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["writer_agent"],
            verbose=True,
        )

    # Define Reviewer Agent
    @agent
    def reviewer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["reviewer_agent"],
            verbose=True,
        )

    # Define Simplifier Agent (simplifies script for learners)
    @agent
    def simplifier_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["simplifier_agent"],
            verbose=True,
            tools=[file_writer_tool],  # Assign FileWriter tool
            
        )
        
    # Define Agent to Save Outputs into YAML
    @agent
    def save_to_yaml_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["save_to_yaml_agent"],
            verbose=True,
            tools=[file_writer_tool],
        )

# ******************* Define Tasks *******************

    # Task to generate the initial podcast script
    @task
    def generate_script_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_script"]
        )

    # Task to review the vocabulary usage in the script
    @task
    def review_script_task(self) -> Task:
        return Task(
            config=self.tasks_config["check_vocabulary_usage"]
        )

    # Task to simplify the script for language learners
    @task
    def simplify_script_task(self) -> Task:
        return Task(
            config=self.tasks_config["simplify_script_learners"]
        )

    # Task to convert the script into audio
    @task
    def convert_script_audio_task(self) -> Task:
        return Task(
            config=self.tasks_config["convert_audio"]
        )
        
    # Task to save the final output into a YAML file
    @task
    def save_to_yaml_task(self) -> Task:
        return Task(
            config=self.tasks_config["save_to_yaml"]
        )

# ******************* Crew Definition *******************

    @crew
    def crew(self) -> Crew:
        """Creates the Vocavoice crew"""

        return Crew(
            agents=self.agents,    # List of agents defined above
            tasks=self.tasks,      # List of tasks defined above
            process=Process.sequential,  # Run tasks one after another
            verbose=True,          # Enable detailed logging
        )
