import oracledb
import pandas as pd

# Conexão com o banco Oracle
conn = oracledb.connect(
    user='rm562274',
    password='090402',
    dsn='oracle.fiap.com.br:1521/ORCL'
)

# Consulta os dados da tabela SENSORES
query = "SELECT * FROM SENSORES"

# Lê os dados em um DataFrame
df = pd.read_sql(query, conn)

# Mostra as 5 primeiras linhas
print(df)

# Fecha a conexão
conn.close()

