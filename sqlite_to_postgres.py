import sqlite3
import pandas as pd
import psycopg2

columns = ['character_id', 'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom']

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

pg_conn = psycopg2.connect(dbname='amrfukiu', user='amrfukiu', password='XnJ75JYw81gP2ye5xICSVYXRS0CDB-YS',
                           host='queenie.db.elephantsql.com')
pg_curs = pg_conn.cursor()

characters_select_query = """
SELECT * FROM charactercreator_character
"""

curs.execute(characters_select_query)
results = curs.fetchall()

sqlite_df = pd.DataFrame(results)

sqlite_df.columns = [columns]

for row in sqlite_df:
    characters_insert_query = """
    INSERT INTO characters ({})
VALUES ({})
    """.format(", ".join(columns), "'" + ", '".join([str(x) for x in row[1]]) + "'")

    pg_curs.execute(characters_insert_query)
    pg_conn.commit()

conn.close()
