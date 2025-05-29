# Criar ambiente virtual
    python -m venv .venv

# Acessar ambiente virtual
    source .venv\Scriptsz\activate

# instalar pacotes nos ambiente virtual
    pip install -r requirements.txt

- Assim tudo fica em um ambiente virtual, visando o controle de versões das bibliotecas usadas.

- deverá ser criado um arquivo .env e conter as API_KEYS dos sistemas (OpenAI, Groq, Tavily e outros)

- padrão de arquivo .env:
    > - GROQ_API_KEY=
    > - OPENAI_API_KEY=
    > - TAVILY_API_KEY=
