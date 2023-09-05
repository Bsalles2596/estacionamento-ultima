import sqlite3






# Conecta-se ao banco de dados
conn = sqlite3.connect('todo.sqlite3')

# Insere uma nova tarefa na tabela tasks
task_name = 'Comprar leite'
due_date = '2023-07-28'
category_id = 1
conn.execute("INSERT INTO tasks (task_name, due_date, category_id) VALUES (?, ?, ?)", (task_name, due_date, category_id))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()
