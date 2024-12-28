import sqlparse
from sqlparse.tokens import Keyword
from sqlparse.sql import Identifier,Parenthesis,IdentifierList,Function

def parse_create_table(query):
    parsed = sqlparse.parse(query)[0]
    tokens = parsed.tokens
    table_seen = False
    table_name_Seen = False
    TABLE_NAME = None
    # print(tokens)
    for t in tokens:
        if(t.ttype is Keyword and t.value.upper() == 'TABLE'):
            table_seen = True
        if(table_seen and isinstance(t, Identifier)):
            table_name_Seen = True
            TABLE_NAME = t.get_real_name()
            print("Table_name",t.get_real_name())
        if(isinstance(t,Parenthesis)):
            result = []        
            for i in t.tokens:
                if(isinstance(i,Identifier)):
                    result.append(i.get_real_name())
                if(isinstance(i,IdentifierList)):
                    for j in i.get_identifiers():
                        if(isinstance(j,Identifier)):
                            result.append(j.get_real_name())
                        if(isinstance(j,Function)):
                            result.append(j.value)
                        if(j.value == 'int'):
                            result.append(j.value)
                        if(j.value == 'class'):
                            result.append(j.value)

                if(isinstance(i,Function)):
                    result.append(i.value)

                if(i.value == 'int'):
                    result.append(i.value)
                if(i.value == 'class'):
                    result.append(i.value)

    result_tuple_list=[]
    for i in range(0,len(result),2):
        result_tuple_list.append((result[i],result[i+1]))

    print("Result tuple list",result_tuple_list)

    def generate_mermaid_er(table_name, columns):
        er_diagram = f"""erDiagram
        {table_name} {{
        """
        for column, data_type in columns:
            er_diagram += f"        {data_type} {column}\n"
        er_diagram += "    }\n"
        return er_diagram

    mermaid_er = generate_mermaid_er(TABLE_NAME, result_tuple_list)
    return mermaid_er