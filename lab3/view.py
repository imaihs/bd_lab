import sys
import pprint
import my_inf



def inf_based():
    field_value = {}
    while (1):
        temp_str = which_you_want_change()
        if(temp_str == "-"):
            break
        field, value = temp_str.split('=')
        field_value.update({field: value})

    return field_value

def inf_for_adding(table_name):
    attrs_class = orm.get_name_attr_of_class(table_name)
    field_value = dict(zip(attrs_class, input_inf_for_table(attrs_class)))
    return field_value

def inf_about_param(str_of_columns, ):
    columns = str_of_columns.split("|")
    dict_of_updating_column = {}
    for column in columns:
        dict_of_updating_column.update({column: inf_for_column(column)})
    return dict_of_updating_column

def search_rows(str_of_columns):
    columns = str_of_columns.split("|")
    dict_of_tacking = {}
    for column in columns:
        type_ = of_column(column)
        match type_:
                case "int":
                    dict_of_tacking[column] = input(f"please input range int numbers for {column} separated by '|'").split("|")
                case "str":
                    dict_of_tacking[column] = input(f"please input scenario for {column} str")
                case "time":
                    dict_of_tacking[column] = input(f"please input range between two dates for {column} separated by '|'").split("|")
    return dict_of_tacking

def of_column(column_name):
    for tables in my_inf.parametrs:
        for parametr in my_inf.parametrs[tables]:
            if(column_name == parametr[0]):
                return parametr[1]
    raise("this column is not exist")
def cmdd_Err():
	print("You have to enter the command from 1 to 5 ERROR")


def comand_identification():
	return input('Enter command : ')

def table_name():
	print('Your table_name name: stadium, ticket, football_match')
	return input('Enter table_name name ')

def print_info(my_dict):
    pprint.pprint(my_dict)

def str_upd():
    return input("Enter column which you want to update separated by'|':")

def colums_str_search():
    return input("Enter column where you want to search values separated by'|':")

def inf_for_column(column_name):
    return input(column_name + ':')

def which_you_want_change():
    return input("Enter colmn atribute,bsed on which you wnt to chnge this fileld like 'Column_name = 'value''and press Enter,whenyou wnt to stop enter columns press '-' and press Enter:")

def Data():
    return input('Enter value: ')

def row():
    return int(input('Enter value: '))

def table_valid():
    print('The table_name name is wrong ERROR')
    sys.exit()

def menu():
    print("Update press 1")
    print("Add press 2")
    print("Delete press 3")
    print("Random press 4")
    print("Search press 5")
    print("Info about tables press 6")
    print("Please print all not numeric types like int and float,like this 'value'")




def print_searc_values(list_of_searching):
    print(list_of_searching)