from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import LLM
import os

@CrewBase
class ResearchAndBlogCrew():
    #path of  config file
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    # Agents
    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'],
            llm=LLM(
                model=os.getenv("MODEL", "gpt-4o-mini"),
                temperature=0.7
            ),
            verbose=True
        )
    
    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['blog_writer'],
            llm=LLM(
                model=os.getenv("MODEL", "gpt-4o-mini"),
                temperature=0.7
            ),
            verbose=True
        )
    
    #tasks
    #order of execution of tasks is report_task followed by blog_writing_task
    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_task']
        )
    
    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_writing_task'],
            output_file="blogs/blog.md"
        )
    
    #crew
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
    