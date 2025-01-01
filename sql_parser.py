import sqlparse
from sqlparse.tokens import Keyword
from sqlparse.sql import Identifier,Parenthesis,IdentifierList,Function

def check_instance_of_token(token):
    val = None
    if(isinstance(token,Identifier)):
        val = token.get_real_name()
    if(isinstance(token,Function) or token.value in keywords):
        val = token.value
    
    return val

def append_token_values(result,token):
    val = check_instance_of_token(token)
    if(isinstance(i,IdentifierList)):
        for j in i.get_identifiers():
            val = check_instance_of_token(j)
            result.append(val)
    elif(val):
        result.append(val)

def generate_mermaid_er(table_name, columns):
    er_diagram = f"""erDiagram
    {table_name} {{
    """
    for column, data_type in columns:
        er_diagram += f"        {data_type} {column}\n"
    er_diagram += "    }\n"
    return er_diagram

tokens = (sqlparse.parse('create table Chaturji(chat varchar(30), users int, cost double);')[0]).tokens
table_seen = False
TABLE_NAME = None
keywords = ['int', 'class', 'double']

for t in tokens:
    if(t.ttype is Keyword and t.value.upper() == 'TABLE'):
        table_seen = True
    if(table_seen and isinstance(t, Identifier)):
        TABLE_NAME = t.get_real_name()
    if(isinstance(t,Parenthesis)):
        result = []     
        val = None
        for i in t.tokens:
            val = None
            append_token_values(result,i)

print("final result",result)
result_tuple_list=[]
for i in range(0,len(result),2):
    result_tuple_list.append((result[i],result[i+1]))
    
print("Result tuple list",result_tuple_list)
mermaid_er = generate_mermaid_er(TABLE_NAME, result_tuple_list)
print(mermaid_er)