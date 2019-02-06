import json
import csv
import sqlite3
import sys

db_file = 'fifa.db'
conn = sqlite3.connect(db_file)


def create_fifa_table():
    """
    Here i am creating the table for my data.
    """
    c = conn.cursor()
    sql_str = """
        create table if not exists fifa (
        id integer primary key autoincrement,
        Name text,
        Age text,
        Nationality text,
        Club text
        );
        """
    c.execute(sql_str)
    conn.commit()


def process_csv_file():

    c = conn.cursor()

    with open('data3/fifa.csv', 'r') as csvfile:

        # parse csv file pointer into hero_stream
        fifa_stream = csv.DictReader(csvfile, delimiter=',', quotechar='"')

        # interate over hero_stream to process.
        for r_ct, fifa_data_row in enumerate(fifa_stream):

            fifa_name = fifa_data_row['Name']
            fifa_age = fifa_data_row['Age']
            fifa_nationality = fifa_data_row['Nationality']
            fifa_club = fifa_data_row['Club']


            # only show the first 20 rows.
            if r_ct <= 50:
                strsql = """
                    insert into fifa ( Name, Age, Nationality, Club) values (
                    '{fifa_name}',
                    '{fifa_age}',
                    '{fifa_nationality}',
                    '{fifa_club}'
                    );
                """.format(
                    fifa_name=fifa_name,
                    fifa_age=fifa_age,
                    fifa_nationality=fifa_nationality,
                    fifa_club=fifa_club
                )
                c.execute(strsql)
                conn.commit()

            # only show the first 20 rows.
            if r_ct <= 20:
                print(r_ct, fifa_name, fifa_age, fifa_nationality, fifa_club)


def main():
    print('Creating a Fifa DB from a csv file.')
    create_fifa_table()
    process_csv_file()

if __name__ == "__main__":
    main()
