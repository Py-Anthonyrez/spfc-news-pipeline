# spfc-news-pipeline
Vou guiar você na criação desse repositório no GitHub, com pipelines em Python usando o Apache Airflow para buscar notícias de compra ou venda de jogadores do São Paulo Futebol Clube nos sites ge.com, cnnbrasil.com.br, gazetaesportiva.com e espn.com.br. Vamos lá:

Crie um Repositório no GitHub:

Acesse o GitHub e faça login ou crie uma conta, caso ainda não tenha.
Clique no botão “New” para criar um novo repositório.
Escolha um nome para o repositório (por exemplo, “spfc-news-pipeline”).
Marque a opção “Initialize this repository with a README”.
Clique em “Create repository”.
Clone o Repositório para o seu Computador:

Abra o terminal ou prompt de comando.
Execute o seguinte comando para clonar o repositório:
git clone https://github.com/seu-usuario/spfc-news-pipeline.git

Estrutura do Projeto:

Dentro da pasta do repositório, crie os seguintes diretórios:
mkdir logs
mkdir data

Configuração do Apache Airflow:

Instale o Apache Airflow:
pip install apache-airflow

Configure o Airflow para usar o banco de dados SQLite ou outro banco de dados de sua preferência.
Crie um arquivo de configuração airflow.cfg com as configurações necessárias.

Crie o arquivo airflow.cfg:

Na raiz do seu projeto, crie um arquivo chamado airflow.cfg.
Este arquivo conterá as configurações necessárias para o Airflow.
Configurações Básicas:

Abra o arquivo airflow.cfg em um editor de texto.

Adicione as seguintes configurações:

[core]
dags_folder = /caminho/para/o/seu/projeto/dags
executor = SequentialExecutor  # Use o SequentialExecutor para testes locais
sql_alchemy_conn = sqlite:///caminho/para/o/seu/projeto/airflow.db

[webserver]
web_server_host = 0.0.0.0
web_server_port = 8080

[scheduler]
job_heartbeat_sec = 5

Substitua /caminho/para/o/seu/projeto pelo caminho real do seu projeto.

Criando um Banco de Dados SQLite:

Instalação:

O SQLite não requer instalação separada. Basta incluir a DLL do SQLite no seu projeto.
Criação do Banco de Dados:

No seu código Python, você pode criar um banco de dados SQLite da seguinte maneira:

Python

import sqlite3

# Conecte-se ao banco de dados (cria um arquivo chamado 'mydatabase.db') Altere o nome para personalizá-lo.
conn = sqlite3.connect('mydatabase.db')

# Crie uma tabela
cursor = conn.cursor()
cursor.execute('''CREATE TABLE jogadores
                   (id INTEGER PRIMARY KEY,
                    nome TEXT,
                    posicao TEXT)''')

# Salve as alterações e feche a conexão
conn.commit()
conn.close()

Manipulação de Dados:

Use comandos SQL padrão para inserir, atualizar e consultar dados na tabela criada.

Inicialize o Banco de Dados:

Execute o seguinte comando para criar o banco de dados SQLite:

airflow db init

Inicie o Airflow Web Server e Scheduler:

Execute os seguintes comandos em terminais separados:

airflow webserver

airflow scheduler

Acesse o Airflow Web UI:

Abra o navegador e acesse http://localhost:8080.
Faça login com as credenciais padrão (usuário: admin, senha: admin).
Você verá o painel do Airflow, onde poderá visualizar e executar suas DAGs.
Teste sua Configuração:

Crie uma DAG de teste e verifique se ela está funcionando corretamente.
Certifique-se de que as tarefas estão sendo executadas e os logs estão sendo salvos na pasta logs.

Crie as DAGs:

Crie arquivos Python para suas DAGs (por exemplo, spfc_news_dag.py).
Defina as tarefas para buscar notícias nos sites especificados.
Salve os dados em arquivos CSV dentro da pasta data.
Automatize a Execução:

Crie um script Python (por exemplo, run_dags.py) que inicia o Airflow e executa as DAGs automaticamente.
Agende a execução diária usando o Scheduler do Airflow.
README.md:

Crie um arquivo README.md na raiz do repositório.
Informe os passos realizados, a finalidade do código e como executar a aplicação.
Inclua detalhes sobre as DAGs, estrutura de pastas, configurações e qualquer outra informação relevante.
Commit e Push:

Adicione todos os arquivos ao repositório:
git add .

Faça o commit:
git commit -m "Adicionando DAGs e configurações"

Envie as alterações para o GitHub:
git push origin master

Agora você tem um repositório com pipelines em Python usando o Apache Airflow para buscar e salvar notícias do São Paulo Futebol Clube automaticamente! 🚀
