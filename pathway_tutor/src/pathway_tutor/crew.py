from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class PathwayTutor():
    """PathwayTutor AI Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def classifier(self) -> Agent:
        """Agent responsible for categorizing the student's question"""
        return Agent(
            config=self.agents_config['classifier'],
            verbose=True
        )

    @task
    def categorize_question(self) -> Task:
        """Task to classify the question into a category"""
        return Task(
            config=self.tasks_config['categorization'],
            description="Analyzes the input question and determines its category, such as Definition-Based, Concept Explanation, Difference-Based, etc.",
            expected_output="A category label that best fits the question type.",
            agent=self.classifier()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PathwayTutor crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
