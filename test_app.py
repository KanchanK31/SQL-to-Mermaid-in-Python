from sql_parser import parse_create_table

def test_create_table():
    ip = """create table Employee(Id int, name varchar(30),department varchar(10),);"""
    op = """erDiagram\n        Employee {\n                int Id\n        varchar(30) name\n        varchar(10) department\n    }\n"""
    print(repr(parse_create_table(ip)))
    assert parse_create_table(ip) == op
