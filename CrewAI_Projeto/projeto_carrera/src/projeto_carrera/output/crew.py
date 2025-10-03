```yaml
tasks:
  - task: Gerenciar a frota de veículos
    description: Monitorar localizações e disponibilidades em tempo real. Tomar decisões sobre envio de veículos a pontos de coleta e entrega.
    inputs:
      - Localização dos veículos
      - Demandas dos usuários
      - Informações de trânsito
    outputs:
      - Veículos enviados para coleta
      - Relatórios de disponibilidade
    responsible_agent: Agente de Transporte

  - task: Monitorar condições das vias
    description: Analisar dados de congestionamentos, acidentes e padrões de movimento para otimizar as rotas.
    inputs:
      - Dados de tráfego
      - Relatórios de acidentes
      - Padrões de movimento
    outputs:
      - Recomendações de rotas
      - Alertas de congestionamentos
    responsible_agent: Agente de Tráfego

  - task: Coletar preferências dos passageiros
    description: Interagir com os passageiros, coletar suas necessidades e feedback sobre a experiência.
    inputs:
      - Solicitações dos usuários
      - Dados de feedback
    outputs:
      - Relatório de preferências dos usuários
      - Sugestões de melhorias
    responsible_agent: Agente de Usuário

  - task: Processar e analisar dados
    description: Analisar grandes volumes de dados históricos e em tempo real para identificar padrões e comportamentos.
    inputs:
      - Dados históricos de transporte
      - Dados em tempo real de uso
    outputs:
      - Padrões de tráfego identificados
      - Recomendações para melhorias no sistema
    responsible_agent: Agente de Análise de Dados

  - task: Fornecer informações e promoções
    description: Entregar dados úteis, promoções e anúncios relevantes aos usuários com base na localização e contexto.
    inputs:
      - Dados de localização dos usuários
      - Anúncios disponíveis
    outputs:
      - Anúncios direcionados
      - Promoções relevantes
    responsible_agent: Agente de Publicidade
```