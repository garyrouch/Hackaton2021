import pandas as pd
from database_construction import insert_information
from Database_creator import create_database
from Database_creator import create_table
from config import CSV_PATH

def add_from_database(csv_file_path):
    df = pd.read_csv(csv_file_path)
    for i in range(len(df)):
        print(df.loc[i])
        email = df.loc[i][0]
        label = df.loc[i][1]
        level = df.loc[i][2]
        insert_information(email = email, label = int(label),  level= int(level))

def main():
    create_database()
    create_table()
    add_from_database(csv_file_path = CSV_PATH )


if __name__ == '__main__':
    main()
