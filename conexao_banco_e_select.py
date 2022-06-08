import MySQLdb

#Variaveis que receberam dados para acesso ao banco de dados
host = "localhost"
user = "root"
password = "chrichri2306"
db = "carros"
port = 3306

#Conexão
con = MySQLdb.connect(host, user, password, db, port)


c = con.cursor()

#Função
def select (fields, tables, where=None):

    global c

    query = " SELECT " + fields + " FROM " + tables
    if(where):
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall() #Pega todos os resultados da função e retorna

print(select("cliente_id, nome", "clientes"))
#cliente_id, nome ---> fields
#clientes ---> tables
#cliente_id = 1 ---> próprio where

result = (select("nome", "clientes"))
print(result[0]) #IMPRIME APENAS O PRIMEIRO ELEMENTO COLETADO DO BANCO