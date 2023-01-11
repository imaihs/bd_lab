parametrs = {
                "stadium": [("id_stadium", "int"), ("adress", "str"), ("number_of_seats", "int")],
                "football_match": [("id_football_match", "int"), ("who_is_play", "str"), ("start_match", "time"), ("end_match", "time"), ("stadium", "int")],
                "ticket": [("id_ticket", "int"), ("cost", "int"), ("seat_in_the_stadium", "int"), ("material", "str"), ("football_match", "int")]
            }

my_inf = {
        "random":
            {
              "stadium":"INSERT INTO stadium (parametrs) SELECT chr(trunc(65+random()*25)::int), trunc(random()*1000)::int",
              "football_match":"INSERT INTO football_match (parametrs) SELECT chr(trunc(65+random()*25)::int), "
                               "timestamp '1970-01-10 20:00:00'+ random() * (timestamp '2033-01-20 20:00:00' - timestamp '1970-01-10 10:00:00'), "
                               "timestamp '1970-01-10 20:00:00'+ random() * (timestamp '2033-01-20 20:00:00' - timestamp '1970-01-10 10:00:00'), "
                               "id_stadium From stadium order by random() limit 1",
              "ticket":"INSERT INTO ticket (parametrs) SELECT trunc(random()*1000)::int,trunc(random()*1000)::int,"
                       "chr(trunc(65+random()*25)::int),id_football_match FROM football_match order by random() limit 1"
            },
        "delete":"delete FROM table_name WHERE str_of_based_column",
        "add_inf":"INSERT INTO table_name (parametrs) VALUES (values)",
        "upd_inf":"UPDATE table_name SET str_of_updating_column WHERE str_of_based_column;",
        "inf":"SELECT param FROM table",
        "presearch":
            [
                "SELECT * FROM stadium, ticket WHERE ",
                "SELECT id_football_match,id_ticket,material,cost FROM football_match, ticket WHERE ",
                "SELECT * FROM football_match,ticket,stadium WHERE "
            ]
    }

random_value_type = {
    'int': "trunc(random()*1000)::int,trunc(random()*1000)::int",
    'str': "chr(trunc(65+random()*25)::int)",
    'data': "timestamp '1970-01-10 20:00:00'+ random() * (timestamp '1971-01-20 20:00:00' - timestamp '1971-01-20 20:00:00')"
                   }