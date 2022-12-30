import psycopg2
import my_inf


def decorator_for_go_to_database(func):
    def wrapper(*args, **kwargs):
        con = psycopg2.connect(
            database="football ticket sales service",
            user="postgres",
            password="password",
            host="localhost",
            port="5432"
        )
        con.set_session(autocommit=True)
        curso_r = con.cursor()
        some_shit = func(con, curso_r, *args, **kwargs)
        curso_r.close()
        con.close()
        return some_shit
    return wrapper



@decorator_for_go_to_database
def random(con, cursor_r, table_name, n):
    param = ",".join([*map(lambda x:my_inf.parametrs[table_name][x][0], range(1, len(my_inf.parametrs[table_name])))])
    try:
        for i in range(int(n)):
            take_sql_string_to_two_stream(cursor_r, my_inf.my_inf["random"][table_name].replace("parametrs", param))
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')

@decorator_for_go_to_database
def add_information(con, cursor_r, table_name, mass):
    param = ",".join([*map(lambda x: my_inf.parametrs[table_name][x][0], range(1, len(my_inf.parametrs[table_name])))])
    mass = [*map(lambda x: "'{0}'".format(x), mass)]
    values = ",".join(mass)
    try:
        take_sql_string_to_two_stream(cursor_r, my_inf.my_inf["add_inf"].replace("table_name", table_name).replace("parametrs", param).replace("values", values))
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')

@decorator_for_go_to_database
def delete(con, cursor_r, table_name, str_of_based_column):
    try:
        take_sql_string_to_two_stream(cursor_r, my_inf.my_inf["delete"].replace("str_of_based_column", str_of_based_column).replace("table_name", table_name))
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')

@decorator_for_go_to_database
def search(con, cursor_r, scenario, dict_of_searching_var):
    list_of_commands = []
    for key, value in dict_of_searching_var.items():
        if(isinstance(value, list)):
            list_of_commands.append(key + " > " + value[0] + " AND " + key + " < " + value[1])
        else:
            list_of_commands.append(key + " LIKE " + value)
    commands = ' AND '.join(list_of_commands)
    try:
        take_sql_string_to_two_stream(cursor_r, my_inf.my_inf["presearch"][scenario] + commands)
        searching_values = cursor_r.fetchall()
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')
    else:
        return searching_values

@decorator_for_go_to_database
def update(con, cursor_r, table_name, str_of_updating_column, str_of_based_column):
    try:
        take_sql_string_to_two_stream(cursor_r, my_inf.my_inf["upd_inf"].replace("table_name", table_name).replace("str_of_updating_column", str_of_updating_column).replace("str_of_based_column", str_of_based_column))
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')


@decorator_for_go_to_database
def information(con, cursor_r):
    dict_of_all_tables = {}
    try:
        for table in my_inf.parametrs:
            dict_of_all_tables[table] = []
            flag_of_take_memory = 1
            for param in my_inf.parametrs[table]:

                param = param[0]
                cursor_r.execute(my_inf.my_inf["inf"].replace("table", table).replace("param", param))
                list_of_all_parametrs = cursor_r.fetchall()

                if (flag_of_take_memory):
                    for memory_take in range(len(list_of_all_parametrs)):
                        dict_of_all_tables[table].append({})
                    flag_of_take_memory = 0
                for i in range(len(list_of_all_parametrs)):
                    dict_of_all_tables[table][i][param] = list_of_all_parametrs[i][0]
            flag_of_take_memory = 1
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')
    else:
        return dict_of_all_tables


def take_sql_string_to_two_stream(cursor_r, sql_stream):
    print(sql_stream)
    cursor_r.execute(sql_stream)

