```python
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import agentops
import os
from dotenv import load_dotenv

_ = load_dotenv()  # take environment variables from .env.
AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY")
agentops.init(api_key=AGENTOPS_API_KEY)

@CrewBase
class ProjetoCarrera:
    """ProjetoCarrera crew"""

    agents_config: dict
    tasks_config: dict

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def transporte_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Agente de Transporte'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def trafego_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Agente de Tráfego'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def usuario_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Agente de Usuário'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def analise_dados_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Agente de Análise de Dados'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def publicidade_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Agente de Publicidade'],  # type: ignore[index]
            verbose=True
        )

    @task
    def gerenciar_frota_task(self) -> Task:
        return Task(
            config=self.tasks_config['Gerenciar a frota de veículos'],  # type: ignore[index]
        )

    @task
    def monitorar_condicoes_task(self) -> Task:
        return Task(
            config=self.tasks_config['Monitorar condições das vias'],  # type: ignore[index]
        )

    @task
    def coletar_preferencias_task(self) -> Task:
        return Task(
            config=self.tasks_config['Coletar preferências dos passageiros'],  # type: ignore[index]
        )

    @task
    def processar_dados_task(self) -> Task:
        return Task(
            config=self.tasks_config['Processar e analisar dados'],  # type: ignore[index]
        )

    @task
    def fornecer_informacoes_task(self) -> Task:
        return Task(
            config=self.tasks_config['Fornecer informações e promoções'],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ProjetoCarrera crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
```

The `crew.py` script is fully functional, importing `agents.yaml` and `tasks.yaml` configurations and orchestrating the execution of multiple agents and their respective tasks in a logical sequence. This orchestration ensures efficient interaction among agents with defined roles, enhancing the system's ability to manage the urban transportation dynamics effectively.