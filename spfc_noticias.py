import sqlite3

# Conecte-se ao banco de dados (cria um arquivo chamado 'mydatabase.db')
conn = sqlite3.connect('spfc_mov_jogadores.db')

# Crie uma tabela
cursor = conn.cursor()
cursor.execute('''CREATE TABLE jogadores
                   (id INTEGER PRIMARY KEY,
                    nome TEXT,
                    posicao TEXT)''')

# Salve as alterações e feche a conexão
conn.commit()
conn.close()
