from model import *
from view import *
import sys


def request():
    while(1):
        menu()
        input_command = comand_identification()

        if (input_command == '1'):
            table = table_name()
            str_of_columns = of_column()
            field_value = inf_about_param(str_of_columns)
            based_field_value = inf_based()
            db.updt(table, field_value, based_field_value)
        elif (input_command == '2'):
            table = table_name()
            field_value = inf_for_adding(table)
            db.add_inf(table, field_value)
        elif (input_command == '3'):
            table = table_name()
            based_field_value = inf_based()
            db.delete(table, based_field_value)
        elif (input_command == '4'):
            table = table_name()
            data = Data()
            db.random(table, data)
        elif (input_command == '6'):
            print_info(search_rows())
        elif (input_command is not str(range(6))):
            cmdd_Err()
            sys.exit()

    sys.exit()

db = DB()
request()