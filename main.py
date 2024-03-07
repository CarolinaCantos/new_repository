import psycopg2

def connect_database(databe_name, user_name, host_name, pass_, port_name):
    conn = psycopg2.connect(database = databe_name,
                            user = user_name,
                            host = host_name,
                            password = pass_,
                            port = port_name)
    return conn

def disconnect_database(conn):
    conn.close()

def update_element(conn, name_table, id, params):
    cmd_sql = f"UPDATE {name_table} SET "
    new_params = []

    for index, (rg, valous) in enumerate(params):
        cmd_sql += f"{rg} = %s"
        new_params.append(valous)
        if index < len(params) - 1:
            cmd_sql += ", "

    cmd_sql += f" WHERE id = {id}"
    cursor = conn.cursor()
    try:
        cursor.execute(cmd_sql, new_params)

        conn.commit()
        print("Atualização realizada com sucesso!")
    except Exception as e:
        print("Erro durante a atualização:", e)
    finally:
        cursor.close()

def insert_element(conn, name_table, params):
    cmd_sql_colunas = "INSERT INTO " + name_table + "("
    cmd_sql_values  = " VALUES ("

    for index_vetor_params, single_param in enumerate(params):
        if index_vetor_params == len(params) - 1:
            cmd_sql_colunas += single_param[0] + ") "
            cmd_sql_values += single_param[1] + ") "
        else:
            cmd_sql_colunas += single_param[0] + ", "
            cmd_sql_values += single_param[1] + ", "

    cmd_sql = cmd_sql_colunas + cmd_sql_values

    cursor = conn.cursor()
    try:
        cursor.execute(cmd_sql)
        print(cmd_sql)
        print("Dados inseridos")
    except Exception as e:
        print(f"Falha: {e}")
    finally:
        conn.commit()
        cursor.close()

def create_table(conn, name_table, params):
    cmd_sql = "CREATE TABLE " + name_table + "("
    for index, p in enumerate(params):
        if index == len(params) -1:
            cmd_sql = cmd_sql + p[0] + " " + p[1]
        else:
            cmd_sql = cmd_sql + p[0] + " " + p[1] + ","
    cmd_sql = cmd_sql + ")"

    cur = conn.cursor()
    
    cur.execute(cmd_sql)
    
    conn.commit()
    cur.close()

if __name__ == '__main__':
    conn = connect_database("TicketController", "postgres", "localhost", "pabd", 5432)
    #create_table(conn, "teste4", [("id", "SERIAL PRIMARY KEY"), ("rg", "INTEGER")])
    #update_element(conn, "teste4", "8", [("rg", "120")])
    insert_element(conn, "teste4", [("id", "3"), ("rg", "116")])
    insert_element(conn, "teste4", [("id", "4"), ("rg", "125")])
    disconnect_database(conn)