import psycopg2
import sqlalchemy

import my_inf
import base
from sqlalchemy import *
import orm



class DB:
    def __init__(self):

        self.session = base.Session()
        self.con = psycopg2.connect(
                    database="football ticket sales service",
                    user="postgres",
                    password="password",
                    host="localhost",
                    port="5432"
                )
        self.con.set_session(autocommit=True)
        self.curso_r = self.con.cursor()



    @staticmethod
    def get_column(con, table, column):
        try:
            cur = con.cursor()
            cur.execute("""SELECT column_name, data_type FROM information_schema.columns
                   WHERE table_name = '{}'""""".format(table))
            for table in cur.fetchall():
                if column in table: return table[1]
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def gen_int(con, rows_number):
        try:
            cur = con.cursor()
            cur.execute("SELECT num "
                        "FROM GENERATE_SERIES(1, {}) AS s(num) "
                        "ORDER BY RANDOM() "
                        "LIMIT {}".format(rows_number, rows_number))
            return cur.fetchall()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def column_data(con, table_name, column_name):
        try:
            cur = con.cursor()
            cur.execute('SELECT {} FROM public."{}"'.format(column_name, table_name))
            values = []
            for val in cur.fetchall():
                values.append(*val)
            return values
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def get_input_format(con, table_name):

        columns = orm.get_class_by_name(table_name).table.columns.keys()
        print(columns)
        return columns

    @staticmethod
    def check_for_presnt(con, column_name, *tabels):
        for el in tabels:
            val_list = []
            print(el)
            columns = con.get_input_format(con, el)
            if column_name not in columns:
                print('{} is not in {} table'.format(column_name, el))
                return False
        return True

    @staticmethod
    def search_between(con, table_name, column_name, limit1, limit2):
        try:
            table_class = orm.get_class_by_name(table_name)
            filter_txt = '{} BETWEEN {} AND {}'.format(column_name, limit1, limit2)
            query = con.query(table_class).filter(text(filter_txt))
            print(*query.all())
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as error:
            print(error)

    @staticmethod
    def search_is_null(con, table_name, column_name):
        try:
            table_class = orm.get_class_by_name(table_name)
            filter_txt = '{} IS NULL'.format(column_name)
            query = con.query(table_class).filter(text(filter_txt))
            print(*query.all())
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as error:
            print(error)

    @staticmethod
    def search_easy(con, table_name, column_name, value):
        try:
            table_class = orm.get_class_by_name(table_name)
            col_name = table_class.dict[column_name]
            filter_txt = '{} = {}'.format(column_name, value)
            query = con.query(table_class).filter(text(filter_txt)).order_by(col_name)
            print(*query.all())
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as error:
            print(error)


    def random_value(self, table_name, n):

        field_type = {my_inf.parametrs[table_name][1:]}

        try:
            for i in range(int(n)):
                self.add(table_name, {field: my_inf.random_value_type[type] for field, type in field_type})
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as err:
            print(err)
            self.session.rollback()
            print(f'WARNING:Error {err}')

    def delete_value(self, table_name, field_value):
        try:
            table_clas = orm.get_class_by_name(table_name)

            filter_txt = dict_to_sql_str(field_value)

            self.session.query(table_clas).filter(text(filter_txt)).delete_value(synchronize_session=False)
            self.session.commit()
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as err:
            print(err)
            self.session.rollback()
            print(f'WARNING:Error {err}')

    def add(self, table_name, field_value):
        try:
            obj = orm.get_class_by_name(table_name)(**field_value)
            self.session.add(obj)
            self.session.commit()
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as err:
            print(err)
            self.session.rollback()
            print(f'WARNING:Error {err}')

    def update(self, table_name, field_value, based_field_value):
        try:
            table_class = orm.get_class_by_name(table_name)

            filter_txt = dict_to_sql_str(based_field_value)

            self.session.query(table_class).filter(text(filter_txt)).update(field_value, synchronize_session=False)

            self.session.commit()

        except (Exception, sqlalchemy.exc.SQLAlchemyError) as err:
            print(err)
            self.session.rollback()
            print(f'WARNING:Error {err}')


    def search_type(self, column_name, *tabels):
        try:
            if self.check_for_presnt(self.session, column_name, *tabels):
                for el in tabels:
                    print("Please input filter type for each column: ")
                    filter = input()
                    if filter.lower() == 'between':
                        print("Please input column name and first and second limits")
                        self.search_between(self.session, el, input(), input(), input())
                    elif filter.lower() == 'is null':
                        print("Please input column name")
                        self.search_is_null(self.session, el, input())
                    elif filter.lower() == 'easy':
                        print("Please input column name and value")
                        self.search_easy(self.session, el, input(), input())
                    else:
                        print("Missing option")
        except(Exception, self.session) as error:
            print(error)
            return False


def dict_to_sql_str(field_value):
    mass_of_filter_str = list(map(lambda key, value: "{} = '{}'".format(key, value), field_value.items()))

    return ' AND '.join(mass_of_filter_str)
