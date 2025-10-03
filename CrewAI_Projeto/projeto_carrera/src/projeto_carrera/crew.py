from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

import agentops
import os
from dotenv import load_dotenv

_ = load_dotenv()  # take environment variables from .env.
AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY")
agentops.init(api_key=AGENTOPS_API_KEY)

# Define your crew here-------------------------------------------------------
@CrewBase
class ProjetoCarrera():
    """ProjetoCarrera crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    
    # agent ------------------------------------------------------------------------
    # 1 ----------------------------------------------------------------------------
    @agent
    def analista_de_negocios(self) -> Agent:
        return Agent(
            config=self.agents_config['analista_de_negocios'], # type: ignore[index]
            verbose=True
        )

    # 2 ----------------------------------------------------------------------------

    @agent
    def arquiteto_de_sistemas(self) -> Agent:
        return Agent(
            config=self.agents_config['arquiteto_de_sistemas'], # type: ignore[index]
            verbose=True
        )
    
    # 3 ----------------------------------------------------------------------------
        
    @agent
    def engenheiro_de_processos(self) -> Agent:
        return Agent(
            config=self.agents_config['engenheiro_de_processos'], # type: ignore[index]
            verbose=True
        )

    # 4 ----------------------------------------------------------------------------

    @agent
    def desenvolvedor_backend(self) -> Agent:
        return Agent(
            config=self.agents_config['desenvolvedor_backend'], # type: ignore[index]
            verbose=True
        )
 
    # 5 ----------------------------------------------------------------------------
        
    @agent
    def qa_testador(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_testador'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    # task -------------------------------------------------------------------------
    # 1 ----------------------------------------------------------------------------
    @task
    def definir_escopo(self) -> Task:
        return Task(
            config=self.tasks_config['definir_escopo'], # type: ignore[index]
            output_file="src/projeto_carrera/output/agents.yaml"
        )

    # 2 ----------------------------------------------------------------------------

    @task
    def modelar_agentes(self) -> Task:
        return Task(
            config=self.tasks_config['modelar_agentes'], # type: ignore[index]
            output_file="src/projeto_carrera/output/tasks.yaml"
        )
    
    # 3 ----------------------------------------------------------------------------
    @task
    def planejar_tarefas(self) -> Task:
        return Task(
            config=self.tasks_config['planejar_tarefas'], # type: ignore[index]
            context=[self.definir_escopo()],
            output_file="src/projeto_carrera/output/crew.py"
        )

    # 4 ----------------------------------------------------------------------------

    @task
    def implementar_orquestracao(self) -> Task:
        return Task(
            config=self.tasks_config['implementar_orquestracao'], # type: ignore[index]
            context=[self.definir_escopo(),
                     self.modelar_agentes()],
            output_file='report.md'
        )
        
    # 5 ----------------------------------------------------------------------------
    
    @task
    def implementar_orquestracao(self) -> Task:
        return Task(
            config=self.tasks_config['implementar_orquestracao'], # type: ignore[index]
            output_file='report.md'
        )
        
    # crew ----------------------------------------------------------------------------  
    
    @crew
    def crew(self) -> Crew:
        """Creates the ProjetoCarrera crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
