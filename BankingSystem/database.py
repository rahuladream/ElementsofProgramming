from sqlite3 import Error
import sqlite3
class Conection:
    def __init__(self):
        self.db_file = 'banking_securet_transaction.db'

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
        return conn
        
    def create_table(self, conn, create_table_sql):
        """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_tables(self, conn):
        """
        1. Create table for banking purpose
        2. Store the customer information
        3. transaction information
        """
        sql_create_customer_table = """ CREATE TABLE IF NOT EXISTS customer (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        account_number integer NOT NULL,
                                        name text NOT NULL,
                                        balance real NOT NULL,
                                        opening_date text
                                    ); """
        sql_create_transaction_table = """ CREATE TABLE IF NOT EXISTS account_transaction (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        account_number integer NOT NULL,
                                        transaction_date text NOT NULL,
                                        transaction_amount text NOT NULL,
                                        FOREIGN KEY (account_number) REFERENCES customer (account_number)
                                    ); """
        sql_create_log_table =   """ CREATE TABLE IF NOT EXISTS transaction_log (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        account_number integer NOT NULL,
                                        whatdone text NOT NULL,
                                        date text NOT NULL,
                                        FOREIGN KEY (account_number) REFERENCES customer (account_number)
                                ); """
    
        if conn is not None:
            # create customer table
            self.create_table(conn, sql_create_customer_table)
            # create transaction table
            self.create_table(conn, sql_create_transaction_table)
            self.create_table(conn, sql_create_log_table)
            return True
        else:
            print('Error ! cannot create the database connection')

    
    def main(self):
        conn=self.create_connection()
        print("Database is live") if self.create_tables(conn) else print("Database is corrupted")
        return conn
